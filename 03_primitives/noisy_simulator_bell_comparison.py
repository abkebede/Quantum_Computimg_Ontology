"""
Bell-state ideal simulator vs noisy simulator comparison.

Purpose:
    Show that real or noisy quantum devices produce small numbers of unexpected
    results such as 01 and 10 for a Bell-state circuit.

Run:
    python 03_primitives\noisy_simulator_bell_comparison.py
"""

from qiskit import QuantumCircuit, transpile


def bell_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


qc = bell_circuit()
print("Bell-state circuit:")
print(qc.draw())

try:
    from qiskit_aer import AerSimulator
    from qiskit_aer.noise import NoiseModel, depolarizing_error, ReadoutError

    ideal_backend = AerSimulator()
    tqc = transpile(qc, ideal_backend)
    ideal_counts = ideal_backend.run(tqc, shots=1000).result().get_counts()

    noise_model = NoiseModel()
    one_qubit_error = depolarizing_error(0.01, 1)
    two_qubit_error = depolarizing_error(0.03, 2)
    readout_error = ReadoutError([[0.98, 0.02], [0.03, 0.97]])
    noise_model.add_all_qubit_quantum_error(one_qubit_error, ["h", "x", "rx", "rz"])
    noise_model.add_all_qubit_quantum_error(two_qubit_error, ["cx"])
    noise_model.add_all_qubit_readout_error(readout_error)

    noisy_backend = AerSimulator(noise_model=noise_model)
    tqc_noisy = transpile(qc, noisy_backend)
    noisy_counts = noisy_backend.run(tqc_noisy, shots=1000).result().get_counts()

    print("Ideal counts:", ideal_counts)
    print("Noisy counts:", noisy_counts)
    print("Expected: ideal counts mostly 00 and 11; noisy counts may include 01 and 10.")
except Exception as exc:
    print("Aer/noise simulation is not available or failed in this environment.")
    print("Error:", exc)
    print("Install or check qiskit-aer if you want to run the noisy comparison.")
