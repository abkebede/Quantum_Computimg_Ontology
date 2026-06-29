"""
Bell-state sampler example.
Concept: Create an entangled state (|00> + |11>)/sqrt(2).
Expected measurement: only 00 and 11, approximately equally often, for ideal simulation.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

sampler = StatevectorSampler(seed=123)
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

print(qc)
print("Measurement counts:", counts)
print("Expected ideal result: approximately half '00' and half '11'.")
