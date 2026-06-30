"""
Heisenberg spin-chain Hamiltonian for a small chain.

Hamiltonian:
    H = J sum_i (X_i X_{i+1} + Y_i Y_{i+1} + Z_i Z_{i+1})

Purpose:
    Introduce spin-chain Hamiltonians used in quantum materials and many-body physics.
"""

from qiskit.quantum_info import SparsePauliOp


def two_pauli_string(n, i, j, op):
    chars = ["I"] * n
    chars[i] = op
    chars[j] = op
    return "".join(chars)


n = 3
J = 1.0
terms = []
for i in range(n - 1):
    for op in ["X", "Y", "Z"]:
        terms.append((two_pauli_string(n, i, i + 1, op), J))

H = SparsePauliOp.from_list(terms)
print("Heisenberg spin-chain Hamiltonian:")
print(H)
print("Number of qubits:", n)
print("Number of Pauli terms:", len(terms))
