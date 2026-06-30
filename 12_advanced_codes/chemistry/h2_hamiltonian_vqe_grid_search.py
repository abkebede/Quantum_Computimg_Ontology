"""
Small H2-style Hamiltonian with a simple VQE-like grid search.

Purpose:
    Show how a molecular Hamiltonian written as Pauli terms can be evaluated with
    a parameterized quantum circuit.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, SparsePauliOp

H2 = SparsePauliOp.from_list([
    ("II", -1.052373245772859),
    ("IZ", 0.39793742484318045),
    ("ZI", -0.39793742484318045),
    ("ZZ", -0.01128010425623538),
    ("XX", 0.18093119978423156),
])


def ansatz(theta0, theta1):
    qc = QuantumCircuit(2)
    qc.ry(theta0, 0)
    qc.ry(theta1, 1)
    qc.cx(0, 1)
    return qc


def energy(theta0, theta1):
    state = Statevector.from_instruction(ansatz(theta0, theta1))
    return float(np.real(state.expectation_value(H2)))

best = None
for theta0 in np.linspace(0, 2 * np.pi, 61):
    for theta1 in np.linspace(0, 2 * np.pi, 61):
        e = energy(theta0, theta1)
        if best is None or e < best[0]:
            best = (e, theta0, theta1)

print("Small H2-style Hamiltonian VQE grid search")
print("Best energy:", best[0])
print("Best theta0:", best[1])
print("Best theta1:", best[2])
print("Best circuit:")
print(ansatz(best[1], best[2]).draw())
