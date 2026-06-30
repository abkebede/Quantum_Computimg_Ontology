"""
Token-safe IBM Quantum hardware comparison template.

Purpose:
    Compare ideal Bell-state simulator counts with real IBM Quantum hardware counts.

Safety:
    Do not paste an IBM Quantum API key into a file that will be uploaded to GitHub.
    Save the account privately on your computer, then load it using QiskitRuntimeService().

Run locally only after your IBM account is saved:
    python 05_ibm_hardware\simulator_vs_hardware_bell_comparison_template.py
"""

from qiskit import QuantumCircuit, transpile
from qiskit.primitives import StatevectorSampler


def bell_circuit() -> QuantumCircuit:
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


qc = bell_circuit()
print("Bell-state circuit:")
print(qc.draw())

sampler = StatevectorSampler()
local_result = sampler.run([qc], shots=1000).result()[0]
print("Local ideal-simulator counts:", local_result.data.c.get_counts())

print("\nHardware section is a template. Uncomment only on a private computer.")
print("Do not upload API keys or token-containing notebooks to GitHub.")

# from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
# service = QiskitRuntimeService()
# backend = service.least_busy(operational=True, simulator=False)
# print("Selected backend:", backend.name)
# transpiled = transpile(qc, backend=backend, optimization_level=1)
# sampler = Sampler(mode=backend)
# job = sampler.run([transpiled], shots=1000)
# print("Job ID:", job.job_id())
# result = job.result()[0]
# print("Hardware counts:", result.data.c.get_counts())
