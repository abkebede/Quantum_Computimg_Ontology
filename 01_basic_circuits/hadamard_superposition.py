"""
One-qubit Hadamard superposition example.
Concept: H|0> = (|0> + |1>)/sqrt(2).
Expected measurement: about half 0 and half 1.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

sampler = StatevectorSampler(seed=123)
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

print(qc)
print("Measurement counts:", counts)
print("Expected: approximately 500 counts for '0' and 500 counts for '1'.")
