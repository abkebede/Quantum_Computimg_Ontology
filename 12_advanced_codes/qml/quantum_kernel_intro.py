"""
Quantum machine-learning kernel intro.

Purpose:
    Compute a simple quantum kernel K(x,y) = |<phi(x)|phi(y)>|^2 using a feature-map circuit.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def feature_map(x):
    qc = QuantumCircuit(2)
    qc.h([0, 1])
    qc.rz(x[0], 0)
    qc.rz(x[1], 1)
    qc.cx(0, 1)
    qc.rz(x[0] * x[1], 1)
    qc.cx(0, 1)
    return qc


def kernel(x, y):
    sx = Statevector.from_instruction(feature_map(x))
    sy = Statevector.from_instruction(feature_map(y))
    return abs(np.vdot(sx.data, sy.data)) ** 2

x = np.array([0.2, 0.7])
y = np.array([0.3, 0.6])
z = np.array([2.0, 1.5])

print("Quantum kernel intro")
print("Feature map for x:")
print(feature_map(x).draw())
print("K(x,y):", kernel(x, y))
print("K(x,z):", kernel(x, z))
print("Interpretation: larger kernel means more similar feature states.")
