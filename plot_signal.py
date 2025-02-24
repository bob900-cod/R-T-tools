import numpy as np
import matplotlib.pyplot as plt
import re
import sys

def parse_formula(formula):
    """
    Analyse la formule pour extraire l'amplitude, la fréquence, la phase et le décalage.
    Gère cos, sin, sinc et portes rectangulaires Π.
    """
    formula = formula.replace(" ", "")  # Supprimer les espaces
    match_cos = re.match(r"([\d.]+)?\*?cos\(2\*?np\.pi\*?([\d.]+)\*?t([+-]?\d*π?/?\d*)?\)", formula)
    match_sin = re.match(r"([\d.]+)?\*?sin\(2\*?np\.pi\*?([\d.]+)\*?t([+-]?\d*π?/?\d*)?\)", formula)
    match_sinc = re.match(r"([\d.]+)?\*?sinc\(2\*?np\.pi\*?([\d.]+)\*?t([+-]?\d*π?/?\d*)?\)", formula)
    match_rect = re.match(r"([\d.]+)?\*?Π([\d.]+)?\(t([+-]?\d*)?\)", formula)

    if match_cos:
        amp = float(match_cos.group(1) or 1)
        freq = float(match_cos.group(2))
        phase = eval(match_cos.group(3).replace("π", "np.pi")) if match_cos.group(3) else 0
        return "cos", amp, freq, phase, 0
    
    elif match_sin:
        amp = float(match_sin.group(1) or 1)
        freq = float(match_sin.group(2))
        phase = eval(match_sin.group(3).replace("π", "np.pi")) if match_sin.group(3) else 0
        return "sin", amp, freq, phase, 0
    
    elif match_sinc:
        amp = float(match_sinc.group(1) or 1)
        freq = float(match_sinc.group(2))
        phase = eval(match_sinc.group(3).replace("π", "np.pi")) if match_sinc.group(3) else 0
        return "sinc", amp, freq, phase, 0
    
    elif match_rect:
        amp = float(match_rect.group(1) or 1)
        width = float(match_rect.group(2) or 1)
        shift = float(match_rect.group(3) or 0)
        return "rect", amp, width, 0, shift

    else:
        raise ValueError("Format non reconnu !")

def plot_signal(formula, time_unit="s"):
    """
    Trace le signal correspondant à la formule donnée.
    L'axe des abscisses peut être en secondes ou en radians.
    """
    signal_type, amp, param1, param2, shift = parse_formula(formula)

    # Temps de -5 à 5 pour les fonctions sinusoïdales et sinc, plus court pour Π
    t = np.linspace(-5, 5, 1000)

    if signal_type == "cos":
        y = amp * np.cos(2 * np.pi * param1 * t + param2)
    
    elif signal_type == "sin":
        y = amp * np.sin(2 * np.pi * param1 * t + param2)
    
    elif signal_type == "sinc":
        t_safe = t + param2  # Décalage en phase
        y = amp * np.sinc(2 * param1 * t_safe)  # sinc(x) = sin(πx) / (πx)
    
    elif signal_type == "rect":
        t = np.linspace(-5, 5, 1000)
        y = amp * ((t >= (shift - param1 / 2)) & (t <= (shift + param1 / 2))).astype(float)
    
    # Création du graphique
    fig, ax = plt.subplots()
    ax.plot(t, y, label=formula, linewidth=2)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.grid(True, linestyle="--", alpha=0.6)

    # Configuration de l'axe des abscisses
    if time_unit == "radian":
        ax.set_xticks(np.arange(-5, 6, 1) * np.pi)
        ax.set_xticklabels([f"{i}π" if i != 0 else "0" for i in range(-5, 6)])
        ax.set_xlabel("Temps (radian)")
    else:
        ax.set_xlabel("Temps (secondes)")

    ax.set_ylabel("Amplitude")
    ax.legend()
    ax.set_title(f"Signal : {formula}")

    # Enable zoom and pan
    plt.subplots_adjust(bottom=0.2)
    ax_zoom = plt.axes([0.81, 0.05, 0.1, 0.075])
    ax_pan = plt.axes([0.7, 0.05, 0.1, 0.075])
    btn_zoom = plt.Button(ax_zoom, 'Zoom')
    btn_pan = plt.Button(ax_pan, 'Pan')

    def zoom(event):
        ax.set_xlim([0, 0.1])
        ax.set_ylim([min(y), max(y)])
        plt.draw()

    def pan(event):
        ax.set_xlim([0, 1])
        ax.set_ylim([min(y), max(y)])
        plt.draw()

    btn_zoom.on_clicked(zoom)
    btn_pan.on_clicked(pan)

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python plot_signal.py '<expression>' <time_unit>")
        sys.exit(1)

    formula = sys.argv[1]
    time_unit = sys.argv[2].strip().lower()
    plot_signal(formula, time_unit)