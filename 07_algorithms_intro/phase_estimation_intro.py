"""
Quantum Phase Estimation intro circuit.

Purpose:
    Demonstrate the structure of phase estimation using a simple controlled phase.
    This example estimates a phase encoded by a unitary acting on a target qubit.
"""

from math import pi
from qiskit import QuantumCircuit
try:
    from qiskit.primitives import StatevectorSampler
except Exception:
    StatevectorSampler = None

qc = QuantumCircuit(3, 2)
# two counting qubits and one target eigenstate qubit
qc.x(2)          # prepare target in |1>, an eigenstate of phase rotations
qc.h(0)
qc.h(1)
# controlled powers of a phase rotation
qc.cp(pi/2, 0, 2)
qc.cp(pi, 1, 2)
# inverse QFT on two counting qubits
qc.h(1)
qc.cp(-pi/2, 0, 1)
qc.h(0)
qc.swap(0, 1)
qc.measure([0, 1], [0, 1])

print("Phase estimation intro circuit:")
print(qc.draw())

if StatevectorSampler is not None:
    sampler = StatevectorSampler()
    result = sampler.run([qc], shots=1000).result()[0]
    print("Counts:", result.data.c.get_counts())
else:
    print("StatevectorSampler not available in this environment.")
