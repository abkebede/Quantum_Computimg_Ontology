"""
Penalty Hamiltonian template for constrained optimization.
Shows how constraints become energy penalties.
"""
from qiskit.quantum_info import SparsePauliOp

# Toy objective/penalty Hamiltonian: H = 1.0 ZZ + 0.5 ZI + 0.5 IZ
H = SparsePauliOp.from_list([
    ("ZZ", 1.0),
    ("ZI", 0.5),
    ("IZ", 0.5),
])
print("Toy penalty Hamiltonian:")
print(H)
print("Teaching point: optimization problems can be encoded as Hamiltonians whose low-energy states are good solutions.")
