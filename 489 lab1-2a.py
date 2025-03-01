import numpy as np
import matplotlib.pyplot as plt

# Define parameters
Fs = 600e6  # Sampling frequency (500 MHz)
T = 1 / Fs
t = np.arange(0, 1e-6, T)  # Time vector (1 microsecond)

# Signals
F1 = 300e6  # 300 MHz
F2 = 800e6  # 800 MHz

x1 = np.cos(2 * np.pi * F1 * t)
x2 = np.cos(2 * np.pi * F2 * t)

# Plot the signals
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x1, label='x1(t) = cos(2π ∙ 300MHz ∙ t)')
plt.title('Signal x1(t)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, x2, label='x2(t) = cos(2π ∙ 800MHz ∙ t)')
plt.title('Signal x2(t)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# FFT to show frequency components
def plot_fft(signal, Fs):
    N = len(signal)
    f = np.fft.fftfreq(N, T)[:N//2]
    fft_vals = np.abs(np.fft.fft(signal))[:N//2]
    plt.plot(f, fft_vals)
    plt.title('Frequency Domain')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid()

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plot_fft(x1, Fs)
plt.title('FFT of x1(t)')

plt.subplot(2, 1, 2)
plot_fft(x2, Fs)
plt.title('FFT of x2(t)')

plt.tight_layout()
plt.show()
