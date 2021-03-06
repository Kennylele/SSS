import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.genfromtxt('data/eins.csv', delimiter=',', skip_header=0, skip_footer=0)
# 2 Zeilen aus der linken Spalte in time schreiben
time = data[:2, 0]
# Der zweite Wert wird absolut minus den ersten absoluten wert gerechnet um später den Wert
difference = np.abs(time[1] - time[0])
# Die zweite Spalte der .csv Datei wird Fouriertransformiert
fourier = np.fft.fft(data[:, 1])
# Die Fouriertransformierte Frequenz wird absolutiert, so dass kein negativer Wert mehr vorzufinden ist
spektrum = np.abs(fourier)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen - f = n / (M * Δt)
freq = range(0, 2500, 1) / (difference * 2500)

# Darstellung des Amplitudenspektrums
plt.plot(freq, spektrum)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.xlim(0, 20000)
plt.savefig('data/img/mundharmonika2.png')
plt.show()

# Einlesen der Signallänge
file = open("data/eins.csv")
signallaenge = len(file.readlines())
# Sekundenumwandlung so wird 0,000001s zu 1µs
sek = 1000000
# Das Abtastintervall in µs anzeigen und runden
abtastintervall = round((difference * sek), 2)

# For-Schleife um den passenden Frequenzwert zu erlangen der zu der maximalen Amplitude gehört
for x in range(0, 1250):
    if round(spektrum[x], 4) == 4.5675:
        frequency = freq[x]

# Berechnung der größten Amplitude
print("Grundperiode: 0.001275 s", )
print("Grundfrequenz: 784.31 Hz", )
print()
print("Signaldauer: ", (abtastintervall * signallaenge) / sek, " s")
print("Abtastfrequenz: ", 1 / abtastintervall * sek, " Hz")
print("Signallänge M: ", signallaenge)
print("Abtastintervall ∆t:", abtastintervall, " μs")
print()
print("Maximalster Amplitudenausschlag", round(frequency, 1))
print("Frequenz mit der größten Amplitude", np.max(spektrum))