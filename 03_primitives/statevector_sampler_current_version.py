"""
Current local sampler pattern using StatevectorSampler.
This file is useful for replacing older examples that used qiskit.primitives.Sampler.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

sampler = StatevectorSampler(default_shots=1024, seed=2026)
job = sampler.run([qc])
result = job.result()
counts = result[0].data.c.get_counts()

print("Circuit:")
print(qc)
print("Counts:", counts)
