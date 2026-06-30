# One-Qubit X Gate and Measurement Counts — Beginner Teaching Unit

## Files Covered

```text
01_basic_circuits/one_qubit_x_gate.py
01_basic_circuits/measurement_counts.py
```

## Level

Beginner.

## Why This Unit Comes First

Before a learner studies superposition, Bell states, Estimator, VQE, or quantum hardware, the learner must understand what a qubit is, what a quantum gate does, what measurement means, and why repeated runs are called shots.

This unit teaches the simplest possible quantum-computing workflow:

```text
create circuit -> apply gate -> measure -> run shots -> read counts
```

## Main Quantum Idea

A qubit starts in the computational basis state `|0>` unless prepared otherwise. The `X` gate flips the qubit:

```text
|0> -> |1>
```

After measurement, the result is stored in a classical bit.

## Important Vocabulary

- **Qubit:** quantum bit used inside a quantum circuit.
- **Classical bit:** ordinary bit used to store measurement results.
- **Gate:** operation applied to a qubit.
- **X gate:** quantum NOT gate; flips `|0>` to `|1>` and `|1>` to `|0>`.
- **Measurement:** process that converts quantum information into a classical outcome.
- **Shot:** one repeated execution of the circuit.
- **Counts:** number of times each bit string appears after many shots.

## Typical Code Pattern

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)

sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()
print(counts)
```

## Line-by-Line Explanation

```python
from qiskit import QuantumCircuit
```

Imports the Qiskit class used to build circuits.

```python
from qiskit.primitives import StatevectorSampler
```

Imports a local simulator-style primitive that samples measurement results from an ideal statevector calculation.

```python
qc = QuantumCircuit(1, 1)
```

Creates a circuit with one qubit and one classical bit.

```python
qc.x(0)
```

Applies the `X` gate to qubit 0. Since the qubit begins in `|0>`, this prepares `|1>`.

```python
qc.measure(0, 0)
```

Measures qubit 0 and stores the result in classical bit 0.

```python
sampler = StatevectorSampler()
```

Creates the sampling object.

```python
job = sampler.run([qc], shots=1000)
```

Runs the circuit 1000 times.

```python
result = job.result()
```

Retrieves the completed result.

```python
counts = result[0].data.c.get_counts()
```

Extracts the measurement counts.

```python
print(counts)
```

Prints the outcome dictionary.

## Expected Output

For the X-gate circuit, the result should be deterministic:

```text
{'1': 1000}
```

or very close to that, depending on the exact simulator and code structure.

For a circuit with no gate before measurement, the result should be:

```text
{'0': 1000}
```

For a circuit with a Hadamard gate, the result becomes probabilistic and should be close to half `0` and half `1`.

## Safe Modifications

### Modification 1 — Remove the X Gate

Change:

```python
qc.x(0)
```

to:

```python
# qc.x(0)
```

Prediction: the qubit stays in `|0>`, so the output should be mostly or entirely `0`.

### Modification 2 — Apply X Twice

Use:

```python
qc.x(0)
qc.x(0)
```

Prediction: the first X changes `|0>` to `|1>`, and the second X changes `|1>` back to `|0>`.

### Modification 3 — Change the Number of Shots

Change:

```python
shots=1000
```

to:

```python
shots=10
```

Prediction: deterministic examples still give the same state, but probabilistic examples fluctuate more when shots are small.

## Unsafe or Confusing Modifications

Do not write:

```python
qc.x(1)
```

if the circuit has only one qubit. Qubit indexing starts at 0, so a one-qubit circuit has only qubit 0.

Do not write:

```python
qc.measure(0, 1)
```

if the circuit has only one classical bit. The only classical bit index is 0.

## Beginner Questions

1. What is the difference between a qubit and a classical bit?
2. Why does `qc.x(0)` make the result `1`?
3. What does `shots=1000` mean?
4. What is the difference between deterministic and probabilistic measurement results?
5. Why does changing one line of code change the physical circuit?

## How This Prepares the Learner

This unit prepares the learner for:

```text
Hadamard superposition
Bell-state entanglement
Sampler outputs
IBM hardware measurement noise
Quantum algorithms based on repeated sampling
```
