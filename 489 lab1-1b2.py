import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

# FIR Filter Coefficients
b_fir = [1, 1, 1, 1, 1]
a_fir = [1]

# IIR Filter Coefficients
b_iir = [1, 1]
a_iir = [1, -1]

# Poles and Zeros
z_fir, p_fir, _ = tf2zpk(b_fir, a_fir)
z_iir, p_iir, _ = tf2zpk(b_iir, a_iir)

# Plot
plt.figure()
plt.scatter(np.real(z_fir), np.imag(z_fir), label='FIR Zeros')
plt.scatter(np.real(p_fir), np.imag(p_fir), label='FIR Poles', marker='x')
plt.scatter(np.real(z_iir), np.imag(z_iir), label='IIR Zeros')
plt.scatter(np.real(p_iir), np.imag(p_iir), label='IIR Poles', marker='x')
plt.title('Poles and Zeros')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid()
plt.legend()
plt.show()
