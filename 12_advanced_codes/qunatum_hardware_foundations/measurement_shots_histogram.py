"""Measurement shots histogram for a single qubit in superposition."""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
shots = 1000
p0 = 0.55
samples = rng.choice(['0', '1'], size=shots, p=[p0, 1-p0])
counts = {bit: int(np.sum(samples == bit)) for bit in ['0','1']}

plt.figure(figsize=(6, 4))
plt.bar(list(counts.keys()), list(counts.values()))
plt.xlabel('Measured bit')
plt.ylabel('Counts')
plt.title('Measurement Outcomes from Repeated Shots')
plt.tight_layout()
plt.show()

print('Counts:', counts)
print('Teaching interpretation: quantum measurement produces a distribution of classical outcomes.')
