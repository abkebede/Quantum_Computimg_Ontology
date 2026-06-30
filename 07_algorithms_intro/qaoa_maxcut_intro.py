"""
Simple QAOA for MaxCut on a 2-node graph.

Purpose:
    Introduce QAOA without relying on high-level algorithm classes.
    The problem is MaxCut for one edge between qubit 0 and qubit 1.

Hamiltonian idea:
    MaxCut reward for one edge is (1 - Z0 Z1)/2.
    We search for parameters gamma and beta that maximize the reward.

Run:
    python 07_algorithms_intro\qaoa_maxcut_intro.py
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, SparsePauliOp


def qaoa_circuit(gamma: float, beta: float) -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.h([0, 1])
    # Cost unitary for one edge. Up to a global phase, this uses RZZ.
    qc.rzz(-gamma, 0, 1)
    # Mixer unitary.
    qc.rx(2 * beta, 0)
    qc.rx(2 * beta, 1)
    return qc


def maxcut_reward(gamma: float, beta: float) -> float:
    qc = qaoa_circuit(gamma, beta)
    state = Statevector.from_instruction(qc)
    zz = SparsePauliOp.from_list([("ZZ", 1.0)])
    zz_expectation = np.real(state.expectation_value(zz))
    return (1.0 - zz_expectation) / 2.0


best = None
for gamma in np.linspace(0, np.pi, 41):
    for beta in np.linspace(0, np.pi / 2, 41):
        reward = maxcut_reward(gamma, beta)
        if best is None or reward > best[0]:
            best = (reward, gamma, beta)

reward, gamma, beta = best
print("Simple QAOA MaxCut example")
print("Best reward:", reward)
print("Best gamma:", gamma)
print("Best beta:", beta)
print("Best circuit:")
print(qaoa_circuit(gamma, beta).draw())
print("Expected: reward close to 1 for the one-edge MaxCut problem.")
