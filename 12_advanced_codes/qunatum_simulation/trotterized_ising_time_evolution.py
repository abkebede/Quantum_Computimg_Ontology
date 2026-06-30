"""
Trotterized two-qubit Ising-style time-evolution circuit.
This is a teaching template for Hamiltonian simulation.
"""
from qiskit import QuantumCircuit
from math import pi

J = 1.0
h = 0.5
dt = 0.2
steps = 2

qc = QuantumCircuit(2)
for _ in range(steps):
    # Approximate exp(-i J Z0 Z1 dt)
    qc.cx(0, 1)
    qc.rz(2 * J * dt, 1)
    qc.cx(0, 1)
    # Approximate transverse-field rotations exp(-i h X dt)
    qc.rx(2 * h * dt, 0)
    qc.rx(2 * h * dt, 1)

print(qc)
print("Teaching point: Trotterization approximates time evolution by splitting Hamiltonian terms.")
