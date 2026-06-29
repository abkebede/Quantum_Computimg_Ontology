"""
One-qubit X gate example.
Concept: The X gate flips |0> to |1>.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)

sampler = StatevectorSampler(seed=123)
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

print(qc)
print("Measurement counts:", counts)
print("Expected: almost all shots should be '1'.")
