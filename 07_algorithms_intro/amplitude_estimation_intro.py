"""
Amplitude estimation intro by repeated sampling.

Purpose:
    Introduce the idea of estimating an unknown probability/amplitude from quantum
    measurements before studying full quantum amplitude estimation algorithms.
"""

from math import asin, sqrt
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

p_true = 0.30
angle = 2 * asin(sqrt(p_true))
qc = QuantumCircuit(1, 1)
qc.ry(angle, 0)
qc.measure(0, 0)

sampler = StatevectorSampler()
shots = 2000
result = sampler.run([qc], shots=shots).result()[0]
counts = result.data.c.get_counts()
ones = counts.get("1", 0)
p_est = ones / shots

print("Amplitude/probability estimation intro")
print(qc.draw())
print("Counts:", counts)
print("Estimated P(1):", p_est)
print("True P(1):", p_true)
print("This is sampling-based estimation, not full quantum amplitude estimation yet.")
