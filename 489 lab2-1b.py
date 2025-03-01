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

Ps = A ** 2 / 2

# Calculate noise variance for target SNR
sigma_squared = Ps / (2 * 10 ** (SNR_dB / 10))

# Add Gaussian noise
noise = np.random.normal(0, np.sqrt(sigma_squared), N)
y = x + noise

# Window functions
windows = {
    'Hanning': np.hanning(N),
    'Hamming': np.hamming(N),
    'Blackman': np.blackman(N)
}

# Plot
plt.figure(figsize=(10, 12))

for i, (window_name, window) in enumerate(windows.items()):
    # Apply window
    y_windowed = y * window

    # Compute the PSD using DFT
    Y_windowed = np.fft.fft(y_windowed)
    PSD_windowed = np.abs(Y_windowed)**2 / N
    frequencies = np.fft.fftfreq(N, 1 / Fs)

    # Calculate window energy
    Ewind = np.sum(window**2)
    
    # Normalize signal power after windowing
    NormPs = Ps * Ewind
    
    # Compute effective SNR after windowing
    SNR_windowed = 10 * np.log10(NormPs / sigma_squared)

    # Plot PSD for each window
    plt.subplot(3, 1, i+1)
    plt.plot(frequencies[:N//2], 10 * np.log10(PSD_windowed[:N//2]))
    plt.title(f"PSD with {window_name} Window")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power (dB)")
    plt.grid(True)

    print(f"SNR with {window_name} window: {SNR_windowed:.2f} dB")

plt.tight_layout()
plt.show()
