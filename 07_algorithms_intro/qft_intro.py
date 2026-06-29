"""
Quantum Fourier Transform introductory example.
This file builds a simple QFT circuit manually for 3 qubits.
"""

from math import pi
from qiskit import QuantumCircuit


def qft(circuit, qubits):
    """Apply QFT to the listed qubits in place."""
    n = len(qubits)
    for j in range(n):
        target = qubits[j]
        circuit.h(target)
        for k in range(j + 1, n):
            control = qubits[k]
            angle = pi / (2 ** (k - j))
            circuit.cp(angle, control, target)
    # Reverse qubit order.
    for j in range(n // 2):
        circuit.swap(qubits[j], qubits[n - j - 1])


qc = QuantumCircuit(3)

# Prepare the computational state |001> by flipping qubit 0.
qc.x(0)

# Apply QFT.
qft(qc, [0, 1, 2])

print(qc)
print("This circuit applies QFT to a 3-qubit input state.")
print("Modify the initial X gates to study different computational-basis inputs.")
