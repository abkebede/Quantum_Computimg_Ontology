"""Toy transmon energy-level visualization.

This is not a full circuit-QED calculation. It illustrates the teaching idea:
Josephson-junction nonlinearity produces anharmonic levels, allowing |0> and |1>
to be addressed as a qubit.
"""
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 6)
omega = 1.0
anharm = 0.08
E_harmonic = omega * (n + 0.5)
E_transmon_like = omega * n - 0.5 * anharm * n * (n - 1)

plt.figure(figsize=(7, 4.5))
for level in E_harmonic:
    plt.hlines(level, 0.1, 0.4)
for level in E_transmon_like:
    plt.hlines(level, 0.6, 0.9)
plt.text(0.25, max(E_harmonic)+0.3, 'Harmonic oscillator', ha='center')
plt.text(0.75, max(E_harmonic)+0.3, 'Transmon-like\nanharmonic levels', ha='center')
plt.text(0.75, E_transmon_like[0], '|0>', va='center')
plt.text(0.75, E_transmon_like[1], '|1>', va='center')
plt.xlim(0, 1)
plt.ylabel('Energy (arb. units)')
plt.title('Why Josephson Nonlinearity Matters')
plt.xticks([])
plt.tight_layout()
plt.show()

print('The qubit uses the two lowest levels. Anharmonic spacing helps isolate the |0> -> |1> transition.')
