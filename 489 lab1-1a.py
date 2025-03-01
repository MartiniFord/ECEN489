import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# FIR Filter Coefficients
b_fir = [0.5, 0.3, 0.2]   # Numerator
a_fir = [1]   # Denominator

# IIR Filter Coefficients
b_iir = [0.5]   # Numerator
a_iir = [1, -0.8]  # Denominator

# Frequency response
w_fir, h_fir = freqz(b_fir, a_fir)
w_iir, h_iir = freqz(b_iir, a_iir)

# Plot the magnitude response
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(w_fir, 20 * np.log10(np.abs(h_fir)), label="FIR Filter")
plt.plot(w_iir, 20 * np.log10(np.abs(h_iir)), label="IIR Filter", linestyle='dashed')
plt.title("Magnitude Response")
plt.xlabel("Normalized Frequency (rad/sample)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid()

plt.show()
