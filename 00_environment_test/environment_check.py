"""
Environment check for the Quantum Computing Code Study Library.
Run:
    python 00_environment_test\environment_check.py
"""

import sys
import importlib.metadata as metadata

print("Python executable:", sys.executable)
print("Python version:", sys.version)

packages = [
    "qiskit",
    "qiskit-aer",
    "qiskit-ibm-runtime",
    "qiskit-algorithms",
    "notebook",
    "ipykernel",
]

for package in packages:
    try:
        print(f"{package}: {metadata.version(package)}")
    except metadata.PackageNotFoundError:
        print(f"{package}: NOT INSTALLED")

from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)
print("\nSimple test circuit:")
print(qc)
