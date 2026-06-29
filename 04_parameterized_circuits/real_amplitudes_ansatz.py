"""
Parameterized ansatz example using RealAmplitudes.
Concept: An ansatz is a tunable quantum circuit used in variational algorithms.
"""

from qiskit.circuit.library import RealAmplitudes

circuit = RealAmplitudes(num_qubits=2, entanglement="linear", reps=1)
params = list(circuit.parameters)
print("Parameters:", params)

# Bind all parameters. The number of values must match the number of circuit parameters.
parameter_values = [3.14, 1.57, 0.50, 2.00]
bound_circuit = circuit.assign_parameters(parameter_values)

print("\nDecomposed bound circuit:")
print(bound_circuit.decompose())
