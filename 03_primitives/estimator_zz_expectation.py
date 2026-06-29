"""
Estimator example: compute <ZZ> for a Bell state.
The Estimator computes expectation values of observables.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

# Build Bell-state circuit without final measurements.
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

observable = SparsePauliOp.from_list([("ZZ", 1.0)])

estimator = StatevectorEstimator()
job = estimator.run([(qc, observable)])
result = job.result()[0]

print(qc)
print("Observable: ZZ")
print("Expectation value <ZZ>:", result.data.evs)
print("Expected: +1 for an ideal Bell state correlated in the Z basis.")
