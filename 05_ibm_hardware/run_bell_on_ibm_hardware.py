"""
Run a Bell-state circuit on IBM Quantum hardware using SamplerV2.

Before running:
1. Create an IBM Quantum account.
2. Save your API key locally using save_ibm_account_template.py.
3. Never upload your real API key to GitHub.
"""

from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

# Load saved IBM Quantum account.
service = QiskitRuntimeService()

# Select a currently available non-simulator backend.
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)
print("Selected backend:", backend.name)

# Build Bell-state circuit.
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Transpile to the selected backend's native gate set and connectivity.
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

# Run with IBM Runtime SamplerV2.
sampler = Sampler(mode=backend)
job = sampler.run([isa_circuit], shots=1024)
print("Submitted job ID:", job.job_id())

result = job.result()
counts = result[0].data.meas.get_counts()
print("Hardware counts:", counts)
print("Expected ideal Bell result: mostly 00 and 11. Extra 01 or 10 counts indicate hardware noise.")
