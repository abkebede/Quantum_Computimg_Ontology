"""
Simplified two-site Hubbard-model teaching Hamiltonian.

Important:
    This is a pedagogical qubit Hamiltonian skeleton, not a full production-grade
    fermion-to-qubit mapping workflow.

Purpose:
    Show how materials/electron-correlation models lead to sums of Pauli terms.
"""

from qiskit.quantum_info import SparsePauliOp

# A small illustrative Pauli Hamiltonian with hopping-like XX/YY terms and interaction-like ZZ terms.
terms = [
    ("XX", -1.0),
    ("YY", -1.0),
    ("ZZ", 0.5),
    ("ZI", 0.25),
    ("IZ", 0.25),
]
H = SparsePauliOp.from_list(terms)
print("Simplified Hubbard-like two-qubit Hamiltonian:")
print(H)
print("Teaching use: connects correlated-electron models to Pauli Hamiltonians.")
