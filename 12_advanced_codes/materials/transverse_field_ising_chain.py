"""
Transverse-field Ising model Hamiltonian for a small spin chain.

Hamiltonian:
    H = -J sum_i Z_i Z_{i+1} - h sum_i X_i

Purpose:
    Introduce materials/condensed-matter Hamiltonians using SparsePauliOp.

Run:
    python 12_advanced_codes\materials\transverse_field_ising_chain.py
"""

from qiskit.quantum_info import SparsePauliOp


def pauli_string(n, position, op):
    chars = ["I"] * n
    chars[position] = op
    return "".join(chars)


def two_pauli_string(n, i, j, op="Z"):
    chars = ["I"] * n
    chars[i] = op
    chars[j] = op
    return "".join(chars)


n = 3
J = 1.0
h = 0.5
terms = []

for i in range(n - 1):
    terms.append((two_pauli_string(n, i, i + 1, "Z"), -J))
for i in range(n):
    terms.append((pauli_string(n, i, "X"), -h))

H = SparsePauliOp.from_list(terms)
print("Transverse-field Ising Hamiltonian:")
print(H)
print("Number of qubits:", n)
print("Number of Pauli terms:", len(terms))
