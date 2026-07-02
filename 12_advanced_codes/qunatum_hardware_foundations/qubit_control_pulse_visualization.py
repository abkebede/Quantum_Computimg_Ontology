"""Visualize idealized microwave control pulses for qubit gates."""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-4, 4, 600)
gaussian = np.exp(-t**2)
drag_like = gaussian * np.sin(4*t)

plt.figure(figsize=(8, 4.5))
plt.plot(t, gaussian, label='Gaussian envelope')
plt.plot(t, drag_like, label='quadrature component')
plt.xlabel('Time')
plt.ylabel('Pulse amplitude')
plt.title('Idealized Microwave Pulse Envelope for a Single-Qubit Gate')
plt.legend()
plt.tight_layout()
plt.show()

print('Teaching interpretation: calibrated pulse amplitude, duration, frequency, and phase implement gate rotations.')
