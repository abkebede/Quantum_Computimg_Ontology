# Teaching Unit: Sampler and StatevectorSampler

## File family

```text
03_primitives/statevector_sampler_current_version.py
03_primitives/sampler_examples.py
03_primitives/estimator_zz_expectation.py
```

## Level

Intermediate beginner.

A learner should first understand:

- qubits
- quantum gates
- measurement
- shots
- counts
- Bell states

## Purpose

This teaching unit explains how a quantum circuit is executed through a primitive that returns measurement outcomes. The Sampler family is the bridge between a circuit diagram and numerical output such as:

```text
{'00': 474, '11': 550}
```

The central idea is:

```text
Build a circuit -> run the circuit many times -> collect outcomes -> interpret probabilities
```

## Conceptual background

A quantum circuit prepares a quantum state. Measurement converts that state into classical bit strings. Since quantum measurement is probabilistic, we usually run the same circuit many times. Each repeated run is called a **shot**.

For a Bell-state circuit, the ideal state is:

```text
(|00> + |11>) / sqrt(2)
```

Therefore, the ideal measured outcomes are only:

```text
00
11
```

The exact number of `00` and `11` results may vary because sampling is statistical.

## Typical code structure

A Sampler example usually has this structure:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

sampler = StatevectorSampler()
job = sampler.run([qc], shots=1024)
result = job.result()
counts = result[0].data.c.get_counts()
print(counts)
```

## Line-by-line explanation

```python
from qiskit import QuantumCircuit
```

Imports the class used to create quantum circuits.

```python
from qiskit.primitives import StatevectorSampler
```

Imports a local primitive that samples measurement results from an ideal statevector simulation.

```python
qc = QuantumCircuit(2, 2)
```

Creates a circuit with two qubits and two classical bits.

```python
qc.h(0)
```

Applies a Hadamard gate to qubit 0. This creates superposition.

```python
qc.cx(0, 1)
```

Applies a controlled-X gate. Qubit 0 controls whether qubit 1 flips. Together with the Hadamard gate, this creates entanglement.

```python
qc.measure([0, 1], [0, 1])
```

Measures both qubits and stores the results in the two classical bits.

```python
sampler = StatevectorSampler()
```

Creates the sampler object.

```python
job = sampler.run([qc], shots=1024)
```

Runs the circuit 1024 times.

```python
result = job.result()
```

Retrieves the completed result.

```python
counts = result[0].data.c.get_counts()
```

Extracts measurement counts from the first circuit result.

```python
print(counts)
```

Displays the measured bit strings and how many times each appeared.

## Expected output

For a Bell-state circuit, expected output is approximately:

```text
{'00': about 512, '11': about 512}
```

A real run may show:

```text
{'00': 474, '11': 550}
```

This is acceptable because sampling has random variation.

## What the learner should notice

The important feature is not exact equality. The important feature is that the only ideal results are:

```text
00 and 11
```

If the simulator output contains only `00` and `11`, the Bell-state correlation is present.

## Safe modifications

### Change the number of shots

```python
job = sampler.run([qc], shots=100)
```

This gives fewer samples and more visible random fluctuation.

```python
job = sampler.run([qc], shots=10000)
```

This gives a distribution closer to the ideal 50/50 result.

### Remove the CX gate

Comment out:

```python
# qc.cx(0, 1)
```

Now the qubits are not entangled. The output should change.

### Move the Hadamard gate

Change:

```python
qc.h(0)
```

to:

```python
qc.h(1)
```

This changes which qubit is placed in superposition. The circuit may no longer create the same Bell state.

## Unsafe or confusing modifications

Avoid these until the learner understands indexing:

```python
qc.h(2)
```

This fails because a two-qubit circuit has only qubits 0 and 1.

Avoid removing classical bits while keeping measurement:

```python
qc = QuantumCircuit(2, 0)
```

The measurement line will fail because there are no classical bits to store the result.

## Sampler versus Estimator

Sampler and Estimator answer different questions.

```text
Sampler question:
What bit strings do I measure, and how often?

Estimator question:
What is the expectation value of a physical or mathematical observable?
```

For example, the Bell-state sampler returns counts such as:

```text
{'00': 501, '11': 499}
```

The Bell-state estimator for the observable `ZZ` returns:

```text
<ZZ> approximately +1
```

Both are correct, but they are different kinds of outputs.

## Why this matters

The primitive layer is where quantum circuits become computational tools. Later examples such as VQE use an Estimator to compute the energy of a Hamiltonian. Optimization examples often use repeated circuit execution to evaluate candidate solutions.

So this unit connects basic circuit learning to scientific and computational applications.

## Student questions

1. What is a shot?
2. Why are counts not exactly 50/50?
3. Why does the Bell-state sampler return only `00` and `11` in an ideal simulation?
4. What changes if the CX gate is removed?
5. What is the difference between Sampler output and Estimator output?
6. Why is this step needed before VQE and quantum optimization?
