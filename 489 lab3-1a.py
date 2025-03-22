import numpy as np
import matplotlib.pyplot as plt

A = 2
f_in = 1e9
f_s = 10e9  
tau = 10e-12
T_sample = 1 / f_s

# Time array for simulation
time_max = 2e-9  # simulation lasts 2 nanoseconds
t = np.linspace(0, time_max, int(time_max / T_sample))

# Input signal
Vin = A * np.sin(2 * np.pi * f_in * t)

# Output signal
Vout = np.zeros_like(t)

# Simulation
last_sample_value = 0
for i in range(len(t)):
    last_sample_value = Vin[i]
    Vout[i] = last_sample_value

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t * 1e9, Vin, label="Input Signal (Vin)", linestyle='--', color='blue')
plt.step(t * 1e9, Vout, label="Output Signal (Vout)", where='post', color='red')
plt.title("Sampling Circuit Output")
plt.xlabel("Time (ns)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()
plt.show()
