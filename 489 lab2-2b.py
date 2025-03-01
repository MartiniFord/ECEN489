import numpy as np
import matplotlib.pyplot as plt

fin = 200e6  
Fs = 420e6  
T_period = 1 / fin  
duration = 5 * T_period  
N_samples = int(Fs * duration)  
t = np.arange(N_samples) / Fs

# Tone
x = np.sin(2 * np.pi * fin * t)

# Compute PSD using DFT
def compute_psd(sig, Fs):
    N = len(sig)
    S = np.fft.fft(sig)
    psd = np.abs(S) ** 2 / N
    freq = np.fft.fftfreq(N, 1/Fs)
    return freq[:N//2], 10 * np.log10(psd[:N//2])

freqs, psd = compute_psd(x, Fs)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(freqs, psd)
plt.title('PSD of the Signal (420 MHz Sampling)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power (dB)')
plt.grid(True)
plt.show()

# Calculate SNR
def calculate_snr(sig, fs):
    Ps = np.mean(sig ** 2)
    Pn = np.mean(np.abs(sig - np.round(sig)) ** 2)
    snr = 10 * np.log10(Ps / Pn)
    return snr

snr = calculate_snr(x, Fs)
print(f"SNR of the signal: {snr:.2f} dB")
