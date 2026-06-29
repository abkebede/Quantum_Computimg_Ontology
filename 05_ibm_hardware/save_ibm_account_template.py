"""
Save IBM Quantum account credentials locally.

IMPORTANT:
- Do not put your real API key in GitHub.
- Do not send your real API key to anyone.
- Run this file only on your private computer, then remove the real token from the file.
"""

from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token="PASTE_YOUR_API_KEY_HERE",
    overwrite=True,
)

print("Account saved locally. Remove the real token from this file before sharing.")
