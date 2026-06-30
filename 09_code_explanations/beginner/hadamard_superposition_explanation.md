# Hadamard Superposition — Complete Beginner Teaching Unit

**Code file:** `01_basic_circuits/hadamard_superposition.py`  
**Level:** Beginner  
**Main idea:** A Hadamard gate changes a qubit prepared in `|0>` into an equal superposition of `|0>` and `|1>`. Measurement converts that quantum state into ordinary classical outcomes.

## 1. Why this example matters

This is one of the first examples every quantum-computing learner should master. It introduces the basic workflow:

```text
create a circuit → apply a gate → measure → run many shots → interpret counts
```

The Hadamard example is important because it shows that a quantum circuit is not merely a deterministic classical program. After the Hadamard gate, a single qubit has two possible measurement outcomes. Repeated runs reveal the probability distribution.

## 2. The code

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

print(qc.draw())

sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

print("Measurement counts:", counts)
print("Expected: approximately 500 counts for '0' and 500 counts for '1'.")
```

## 3. Line-by-line explanation

### `from qiskit import QuantumCircuit`

This imports the `QuantumCircuit` class from Qiskit. A `QuantumCircuit` is the main object used to build a quantum program.

### `from qiskit.primitives import StatevectorSampler`

This imports `StatevectorSampler`, a current Qiskit primitive for sampling measurement results from quantum circuits using ideal statevector simulation.

### `qc = QuantumCircuit(1, 1)`

This creates a circuit with:

```text
1 qubit
1 classical bit
```

The qubit stores the quantum state. The classical bit stores the final measurement result.

### `qc.h(0)`

This applies a Hadamard gate to qubit `0`.

The qubit starts in `|0>`. After the Hadamard gate, the state becomes:

```text
(|0> + |1>) / sqrt(2)
```

This means the measurement probabilities are:

```text
P(0) = 1/2
P(1) = 1/2
```

### `qc.measure(0, 0)`

This measures qubit `0` and stores the result in classical bit `0`.

The first `0` means qubit index 0. The second `0` means classical-bit index 0.

### `print(qc.draw())`

This prints a text drawing of the quantum circuit. A typical output is:

```text
     ┌───┐┌─┐
  q: ┤ H ├┤M├
     └───┘└╥┘
c: 1/══════╩═
           0
```

### `sampler = StatevectorSampler()`

This creates the sampler object. The sampler runs the circuit many times and returns measurement counts.

### `job = sampler.run([qc], shots=1000)`

This runs the circuit 1000 times.

Each run is called a **shot**. With 1000 shots, the result should be close to 500 zeros and 500 ones.

### `result = job.result()`

This retrieves the completed result from the sampler job.

### `counts = result[0].data.c.get_counts()`

This extracts the measurement counts from the result.

The keys are measured bit strings:

```text
'0'
'1'
```

The values are the number of times each result appeared.

### `print("Measurement counts:", counts)`

This prints the final measured counts.

## 4. Tested output

A tested output from this repository was:

```text
Measurement counts: {'1': 499, '0': 501}
Expected: approximately 500 counts for '0' and 500 counts for '1'.
```

This is exactly what the Hadamard superposition should produce.

## 5. Python syntax used

| Syntax | Meaning |
|---|---|
| `from ... import ...` | Import a class or function from a package |
| `qc = QuantumCircuit(1, 1)` | Create an object and assign it to a variable |
| `qc.h(0)` | Call a method on the circuit object |
| `sampler.run([qc], shots=1000)` | Run a method with arguments |
| `result[0]` | Access the first result item |
| `print(...)` | Display output |

## 6. Qiskit syntax used

| Qiskit syntax | Meaning |
|---|---|
| `QuantumCircuit(1, 1)` | Create a one-qubit, one-classical-bit circuit |
| `qc.h(0)` | Apply Hadamard gate to qubit 0 |
| `qc.measure(0, 0)` | Measure qubit 0 into classical bit 0 |
| `StatevectorSampler()` | Create an ideal sampler |
| `shots=1000` | Repeat the circuit 1000 times |
| `get_counts()` | Return measurement counts |

## 7. Quantum meaning

The Hadamard gate creates a superposition. Before measurement, the qubit is not simply classical 0 or classical 1. The quantum state has amplitudes for both outcomes. Measurement produces one classical bit at a time, but many repeated measurements reveal the probability distribution.

## 8. Safe modifications

### Modification A — Change the number of shots

Change:

```python
job = sampler.run([qc], shots=1000)
```

to:

```python
job = sampler.run([qc], shots=100)
```

Expected result: still approximately 50/50, but with larger random fluctuations.

Change it to:

```python
job = sampler.run([qc], shots=10000)
```

Expected result: closer to 50/50.

### Modification B — Remove the Hadamard gate

Change:

```python
qc.h(0)
```

to:

```python
# qc.h(0)
```

Expected result: the qubit remains in `|0>`, so almost all counts should be `0`.

### Modification C — Replace Hadamard with X

Change:

```python
qc.h(0)
```

to:

```python
qc.x(0)
```

Expected result: the qubit becomes `|1>`, so almost all counts should be `1`.

## 9. Unsafe or confusing modifications

Do not change this line casually:

```python
qc = QuantumCircuit(1, 1)
```

If you write:

```python
qc = QuantumCircuit(1, 0)
```

then the circuit has no classical bit, and measurement into classical bit 0 will fail.

Do not write:

```python
qc.h(1)
```

because the circuit has only one qubit, indexed as `0`.

## 10. Beginner questions

1. What does the Hadamard gate do to `|0>`?
2. Why are the counts not exactly 500 and 500 every time?
3. What is a shot?
4. What is the difference between a qubit and a classical bit?
5. What happens if the Hadamard gate is removed?
6. What happens if the Hadamard gate is replaced by an X gate?
7. Why is this example a starting point for quantum random sampling?

## 11. Application connection

This code does not solve a large real-world problem by itself. Its value is foundational. It teaches quantum sampling, measurement, and probabilistic outputs. These ideas appear later in quantum algorithms for search, optimization, chemistry, materials, simulation, and machine learning.

## 12. Where this example fits in the learning path

```text
environment setup
→ one-qubit gates
→ Hadamard superposition
→ measurement counts
→ Bell states
→ Sampler and Estimator
→ Hamiltonians
→ VQE and applications
```

This is the first complete beginner teaching unit in the QC Code Study Library.
