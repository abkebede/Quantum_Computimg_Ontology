"""
Three-qubit bit-flip repetition code teaching example.
This is a conceptual error-correction example, not a full fault-tolerant circuit.
"""
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(3, 3)

# Encode logical |1> as |111>. Change/comment this X to study logical |0>.
qc.x(0)
qc.cx(0, 1)
qc.cx(0, 2)

# Simulate a bit-flip error on qubit 1.
qc.x(1)

# Decode by reversing the encoding structure.
qc.cx(0, 2)
qc.cx(0, 1)

# This simple circuit shows that error correction requires syndrome logic;
# decoding alone is not a complete correction procedure.
qc.measure([0, 1, 2], [0, 1, 2])

print(qc)
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
counts = job.result()[0].data.c.get_counts()
print("Counts:", counts)
print("Teaching point: bit-flip protection requires encoding, syndrome extraction, and correction.")
