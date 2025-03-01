import numpy as np
import matplotlib.pyplot as plt

A = 1
fin = 2e6
Fs = 5e6
SNR_dB = 50
T = 1e-3
N = int(Fs * T)
t = np.arange(N) / Fs

# Tone
x = A * np.sin(2 * np.pi * fin * t)

# Compute Ps
Ps = A ** 2 / 2

# Calculate noise variance for target SNR
N_var = Ps / (2 * 10 ** (SNR_dB / 10))

# Add Gaussian noise
noise = np.random.normal(0, np.sqrt(N_var), N)
y = x + noise

# Calculate PSD using DFT
Y = np.fft.fft(y)
PSD = np.abs(Y)**2 / N  # Normalize by # of samples
frequencies = np.fft.fftfreq(N, 1 / Fs)

# Plot PSD
plt.figure(figsize=(10, 6))
plt.plot(frequencies[:N//2], 10 * np.log10(PSD[:N//2]))
plt.title("PSD with Gaussian Noise")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (dB)")
plt.grid(True)
plt.show()

# Variance for uniformly distributed noise for same SNR
a_uniform = np.sqrt(3 * N_var)
print(f"Variance of uniformly distributed noise: {N_var:.6f}")
print(f"Amplitude range for uniform noise: {a_uniform:.6f}")
