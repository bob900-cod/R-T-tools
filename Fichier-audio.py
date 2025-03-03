import numpy as np
import matplotlib.pyplot as plt
import scipy as sy
import soundfile as sf
import sys

if len(sys.argv) != 2:
    print("Usage: python Audio_file.py <audio_filename>")
    sys.exit(1)

audio_filename = sys.argv[1]

data, fe = sf.read(audio_filename)
start_sample = 10 * fe 
end_sample = 12 * fe   

segment = data[start_sample:end_sample]
plt.figure(figsize=(10, 4))
plt.plot(segment)
plt.title("Signal audio entre 10 et 12 secondes")
plt.xlabel("Échantillons")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

segment = data[start_sample:end_sample]

n = len(segment)  
fft_data = np.fft.fft(segment)  
frequencies = np.fft.fftfreq(n, 1/fe) 

positive_frequencies = frequencies[:n // 2]
positive_fft = fft_data[:n // 2]

power_spectral_density = np.abs(positive_fft) ** 2 / n 

power_spectral_density_dbm = 10 * np.log10(power_spectral_density * 1000)  
plt.figure(figsize=(10, 6))
plt.plot(positive_frequencies, power_spectral_density_dbm)
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Densité Spectrale de Puissance (dBm)")
plt.grid(True)
plt.xlim(0, fe / 2) 
plt.show()

bande_frequences = (positive_frequencies[0], positive_frequencies[-1])
print(f"Bande de fréquence du signal: {bande_frequences[0]:.2f} Hz à {bande_frequences[1]:.2f} Hz")
