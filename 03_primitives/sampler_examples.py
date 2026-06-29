"""
Sampler examples with current local Qiskit reference primitive: StatevectorSampler.
The sampler returns measurement samples/counts from circuits with measurement.
"""

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

circuits = []

# Circuit 1: deterministic |0>
qc0 = QuantumCircuit(1, 1)
qc0.measure(0, 0)
circuits.append(qc0)

# Circuit 2: deterministic |1>
qc1 = QuantumCircuit(1, 1)
qc1.x(0)
qc1.measure(0, 0)
circuits.append(qc1)

# Circuit 3: superposition
qch = QuantumCircuit(1, 1)
qch.h(0)
qch.measure(0, 0)
circuits.append(qch)

sampler = StatevectorSampler(seed=7)
job = sampler.run(circuits, shots=1000)
result = job.result()

for i, circuit in enumerate(circuits):
    print(f"\nCircuit {i}")
    print(circuit)
    print(result[i].data.c.get_counts())
