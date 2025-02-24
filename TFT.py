import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift
import sys
import re

def parse_formula(formula):
    """
    Analyse la formule pour extraire l'amplitude, la fréquence, la phase et le décalage.
    Gère cos et sin.
    """
    formula = formula.replace(" ", "")  # Supprimer les espaces
    match_cos = re.match(r"([\d.]+)?\*?cos\(2\*?np\.pi\*?([\d.]+)\*?t([+-]?\d*π?/?\d*)?\)", formula)
    match_sin = re.match(r"([\d.]+)?\*?sin\(2\*?np\.pi\*?([\d.]+)\*?t([+-]?\d*π?/?\d*)?\)", formula)

    if match_cos:
        amp = float(match_cos.group(1) or 1)
        freq = float(match_cos.group(2))
        phase = eval(match_cos.group(3).replace("π", "np.pi")) if match_cos.group(3) else 0
        return "cos", amp, freq, phase
    
    elif match_sin:
        amp = float(match_sin.group(1) or 1)
        freq = float(match_sin.group(2))
        phase = eval(match_sin.group(3).replace("π", "np.pi")) if match_sin.group(3) else 0
        return "sin", amp, freq, phase

    else:
        raise ValueError("Format non reconnu !")

def plot_fourier_transform(formula):
    """
    Trace la transformée de Fourier du signal correspondant à la formule donnée.
    """
    signal_type, amp, freq, phase = parse_formula(formula)

    # Paramètres de l'échantillonnage
    fe = 10 * freq  # Fréquence d'échantillonnage (10 fois la fréquence du signal)
    Te = 1 / fe  # Période d'échantillonnage
    N = 1024  # Nombre de points de la FFT
    t = np.arange(0, N * Te, Te)  # Temps

    # Génération du signal
    if signal_type == "cos":
        signal = amp * np.cos(2 * np.pi * freq * t + phase)
    elif signal_type == "sin":
        signal = amp * np.sin(2 * np.pi * freq * t + phase)

    # Calcul de la FFT
    signal_fft = fft(signal)
    freqs = fftfreq(N, Te)  # Fréquences associées
    signal_fft_shifted = fftshift(signal_fft)  # Décalage pour centrer la FFT
    freqs_shifted = fftshift(freqs)  # Décalage des fréquences

    # Tracé du spectre en amplitude
    plt.figure(figsize=(10, 5))
    plt.plot(freqs_shifted, np.abs(signal_fft_shifted) / N, color='b')
    plt.xlabel('Fréquence (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Transformée de Fourier du signal')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python TFT.py '<expression>'")
        sys.exit(1)

    formula = sys.argv[1]
    plot_fourier_transform(formula)