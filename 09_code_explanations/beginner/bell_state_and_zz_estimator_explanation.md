# Bell State and ZZ Estimator — Complete Teaching Unit

## Code files

- `02_bell_states/bell_state_sampler.py`
- `03_primitives/estimator_zz_expectation.py`

## Level

Beginner to intermediate.

This teaching unit begins with a two-qubit Bell-state circuit and then uses the Estimator primitive to compute the expectation value of the observable `ZZ`. The Bell-state code teaches entanglement through measurement counts. The Estimator code teaches how quantum circuits can be used to compute a physical quantity.

## Learning goals

After working through this unit, a learner should be able to:

1. Build a two-qubit Bell-state circuit.
2. Explain the role of the Hadamard gate and controlled-X gate.
3. Interpret why the ideal Bell state produces only `00` and `11` outcomes.
4. Explain the difference between measurement counts and expectation values.
5. Use `SparsePauliOp` to define the observable `ZZ`.
6. Interpret why the Bell state has `<ZZ> = +1`.
7. Modify the circuit one line at a time and predict how the output changes.

## Part 1 — Bell-state sampler code

The Bell-state sampler code prepares and measures the Bell state:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

print(qc.draw())

sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()
print("Measurement counts:", counts)
print("Expected ideal result: approximately half '00' and half '11'.")
```

## Line-by-line explanation

```python
from qiskit import QuantumCircuit
```

Imports the Qiskit class used to create a quantum circuit.

```python
from qiskit.primitives import StatevectorSampler
```

Imports the current local sampler primitive. A sampler returns measurement outcomes from a quantum circuit.

```python
qc = QuantumCircuit(2, 2)
```

Creates a circuit with two qubits and two classical bits.

```python
qc.h(0)
```

Applies a Hadamard gate to qubit 0. This changes qubit 0 from `|0>` into an equal superposition of `|0>` and `|1>`.

```python
qc.cx(0, 1)
```

Applies a controlled-X gate. Qubit 0 is the control and qubit 1 is the target. If qubit 0 is `1`, qubit 1 flips. This gate entangles the two qubits.

```python
qc.measure([0, 1], [0, 1])
```

Measures qubits 0 and 1 and stores the results in classical bits 0 and 1.

```python
sampler = StatevectorSampler()
```

Creates the sampler object.

```python
job = sampler.run([qc], shots=1000)
```

Runs the circuit 1000 times. Each run is called a shot.

```python
result = job.result()
counts = result[0].data.c.get_counts()
```

Retrieves the measurement counts.

## Expected Bell-state result

The ideal Bell state is:

```text
(|00> + |11>) / sqrt(2)
```

Therefore the expected measurement outcomes are:

```text
00 about 50 percent
11 about 50 percent
01 approximately 0 percent
10 approximately 0 percent
```

A successful ideal simulator run may look like:

```text
Measurement counts: {'11': 499, '00': 501}
```

## Part 2 — ZZ Estimator code

The Estimator example uses the same Bell state, but does not measure counts. Instead, it computes the expectation value of an observable:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorEstimator
from qiskit.quantum_info import SparsePauliOp

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

observable = SparsePauliOp.from_list([("ZZ", 1.0)])

estimator = StatevectorEstimator()
job = estimator.run([(qc, observable)])
result = job.result()
value = result[0].data.evs

print(qc.draw())
print("Observable: ZZ")
print("Expectation value <ZZ>:", value)
print("Expected: +1 for an ideal Bell state correlated in the Z basis.")
```

## Line-by-line explanation of the Estimator part

```python
from qiskit.primitives import StatevectorEstimator
```

Imports the Estimator primitive. The Estimator computes expectation values, not measurement count dictionaries.

```python
from qiskit.quantum_info import SparsePauliOp
```

Imports the class used to define observables such as `Z`, `ZZ`, `XX`, and Hamiltonians.

```python
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
```

Creates the same Bell state, but without final classical measurement bits. Estimator calculations usually act on the quantum state before measurement.

```python
observable = SparsePauliOp.from_list([("ZZ", 1.0)])
```

Defines the observable `ZZ`. This means Pauli-Z on qubit 0 and Pauli-Z on qubit 1.

```python
estimator = StatevectorEstimator()
job = estimator.run([(qc, observable)])
```

Runs the Estimator for the pair: circuit and observable.

```python
value = result[0].data.evs
```

Extracts the expectation value.

## Meaning of `<ZZ>`

For the Bell state:

```text
(|00> + |11>) / sqrt(2)
```

The `ZZ` observable gives:

```text
00: (+1)(+1) = +1
11: (-1)(-1) = +1
```

Both allowed Bell-state outcomes contribute `+1`, so:

```text
<ZZ> = +1
```

A typical output is:

```text
Expectation value <ZZ>: 0.9999999999999998
```

This is equal to `1.0` within ordinary floating-point rounding.

## Python syntax to notice

- `import` statements bring Qiskit classes into the program.
- `qc = QuantumCircuit(2, 2)` creates an object.
- `qc.h(0)` calls a method on the circuit object.
- `qc.cx(0, 1)` uses qubit index 0 as control and qubit index 1 as target.
- Lists such as `[0, 1]` are used to refer to multiple qubits or classical bits.
- Dictionaries such as `{'00': 501, '11': 499}` store measurement outcomes and counts.

## Qiskit syntax to notice

- `QuantumCircuit(2, 2)` means two qubits and two classical bits.
- `h(0)` applies the Hadamard gate to qubit 0.
- `cx(0, 1)` applies controlled-X with control qubit 0 and target qubit 1.
- `measure([0, 1], [0, 1])` measures both qubits.
- `StatevectorSampler()` returns sampled counts for measured circuits.
- `StatevectorEstimator()` returns expectation values for observables.
- `SparsePauliOp.from_list([("ZZ", 1.0)])` defines a two-qubit observable.

## Safe modifications

### Modification 1 — Remove the CX gate

Change:

```python
qc.cx(0, 1)
```

to:

```python
# qc.cx(0, 1)
```

Prediction: the qubits are no longer entangled. The first qubit is in superposition, but the second qubit remains `0`. Expected outcomes are mostly `00` and `01` or `00` and `10`, depending on bit-order display.

### Modification 2 — Change the control and target

Change:

```python
qc.cx(0, 1)
```

to:

```python
qc.cx(1, 0)
```

Prediction: since qubit 1 has not been placed into superposition, this no longer creates the same Bell state.

### Modification 3 — Change the observable

Change:

```python
observable = SparsePauliOp.from_list([("ZZ", 1.0)])
```

to:

```python
observable = SparsePauliOp.from_list([("XX", 1.0)])
```

Prediction: this tests correlation in the X basis instead of the Z basis. For a Bell state, this is also meaningful.

### Modification 4 — Change the number of shots

Change:

```python
job = sampler.run([qc], shots=1000)
```

to:

```python
job = sampler.run([qc], shots=100)
```

Prediction: the same outcomes appear, but the 50/50 split fluctuates more.

## Unsafe or confusing modifications

- Do not use `qc.h(2)` in a two-qubit circuit. Qubit index 2 does not exist.
- Do not define `QuantumCircuit(2, 0)` and then try to measure into classical bits.
- Do not use a three-letter observable such as `ZZZ` for a two-qubit circuit.
- Do not mix Sampler output syntax with Estimator output syntax; they return different result structures.

## Beginner questions

1. What does the Hadamard gate do before the CX gate?
2. Why does `qc.cx(0, 1)` create correlation between the qubits?
3. Why are `01` and `10` absent in the ideal Bell-state result?
4. What is the difference between measurement counts and an expectation value?
5. Why does `<ZZ>` equal `+1` for the Bell state?
6. What happens if the CX gate is removed?
7. What happens if the number of shots is changed from 1000 to 100?

## Application connection

Bell states are not yet an application by themselves, but they are a foundation for important quantum information tasks:

- quantum teleportation
- superdense coding
- entanglement-based communication
- quantum error correction
- Bell inequality tests
- quantum networking
- correlation measurements in many-qubit systems

For the code library, this teaching unit is the bridge between simple one-qubit circuits and application-oriented quantum algorithms that use observables, Hamiltonians, and correlations.
