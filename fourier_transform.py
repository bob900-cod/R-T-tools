import pandas as pd
import matplotlib.pyplot as plt

# Données du tableau
data = {
    "u(t)": [
        "A",
        "e^(j2πf₀t)",
        "cos(2πf₀t)",
        "sin(2πf₀t)",
        "ΠT₀(t)",
        "δ(t)"
    ],
    "U(f)": [
        "A δ(f)",
        "δ(f - f₀)",
        "1/2 [δ(f + f₀) + δ(f - f₀)]",
        "1/2j [δ(f - f₀) - δ(f + f₀)]",
        "T₀ sinc(πfT₀)",
        "1"
    ],
    "|U(f)|": [
        "A δ(f)",
        "δ(f - f₀)",
        "1/2 [δ(f + f₀) + δ(f - f₀)]",
        "1/2 [δ(f + f₀) + δ(f - f₀)]",
        "|T₀ sinc(πfT₀)|",
        "1"
    ]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Affichage du tableau
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

plt.show()