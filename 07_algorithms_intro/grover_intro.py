"""
Introductory Grover search example for two qubits.
Target state: |11>.
This is a small educational circuit, not a scalable implementation.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)

# 1. Create equal superposition over 00, 01, 10, 11.
qc.h([0, 1])

# 2. Oracle: mark |11> by applying a controlled-Z.
qc.cz(0, 1)

# 3. Diffusion operator for two qubits.
qc.h([0, 1])
qc.x([0, 1])
qc.h(1)
qc.cx(0, 1)
qc.h(1)
qc.x([0, 1])
qc.h([0, 1])

# 4. Measure.
qc.measure([0, 1], [0, 1])

sampler = StatevectorSampler(seed=123)
result = sampler.run([qc], shots=1000).result()
counts = result[0].data.c.get_counts()

print(qc)
print("Counts:", counts)
print("Expected: the target state '11' should dominate.")
