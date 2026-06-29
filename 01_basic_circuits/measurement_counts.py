"""
Measurement-counts example.
Try modifying apply_h and shots.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

apply_h = True
shots = 2000

qc = QuantumCircuit(1, 1)
if apply_h:
    qc.h(0)
qc.measure(0, 0)

sampler = StatevectorSampler(seed=42)
job = sampler.run([qc], shots=shots)
result = job.result()
counts = result[0].data.c.get_counts()

print(qc)
print("Shots:", shots)
print("Measurement counts:", counts)
print("Modify apply_h = False to see the qubit stay in |0>.")
