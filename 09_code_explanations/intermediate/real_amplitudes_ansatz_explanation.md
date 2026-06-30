# RealAmplitudes Parameterized Ansatz — Line-by-Line Teaching Unit

## Code file

```text
04_parameterized_circuits/real_amplitudes_ansatz.py
```

## Level

Intermediate.

This example comes after one-qubit circuits, Bell states, Sampler, and Estimator examples. It introduces the idea of a **parameterized quantum circuit**, also called an **ansatz**.

## What the code does

The code builds a two-qubit parameterized circuit using Qiskit's `RealAmplitudes` circuit template. It then assigns numerical values to the circuit parameters and prints the decomposed circuit.

A parameterized circuit is a circuit whose gates contain adjustable angles. Instead of hardcoding all gates with fixed values, the circuit contains symbolic parameters such as:

```text
θ[0], θ[1], θ[2], θ[3]
```

These parameters can later be changed by a classical optimizer.

## Why this example matters

Parameterized circuits are the bridge from simple circuit demonstrations to real quantum algorithms. They are used in:

```text
VQE — Variational Quantum Eigensolver
QAOA — Quantum Approximate Optimization Algorithm
quantum machine learning
variational quantum simulation
noise-aware hybrid quantum algorithms
```

The main idea is:

```text
fixed quantum circuit structure + adjustable parameters = trainable quantum model
```

## Core Qiskit syntax

### Importing the ansatz template

```python
from qiskit.circuit.library import RealAmplitudes
```

This imports a built-in Qiskit circuit template. `RealAmplitudes` creates a parameterized circuit using real-valued rotation gates and entangling gates.

### Creating the circuit

```python
circuit = RealAmplitudes(num_qubits=2, entanglement="linear", reps=1)
```

This creates a two-qubit ansatz circuit.

The arguments mean:

```text
num_qubits=2          use two qubits
entanglement="linear" connect neighboring qubits with entangling gates
reps=1                use one repetition layer
```

For two qubits, the circuit typically contains rotation gates and one entangling operation.

### Listing parameters

```python
params = list(circuit.parameters)
print("Parameters:", params)
```

This lists the symbolic parameters inside the circuit. A typical output is:

```text
[θ[0], θ[1], θ[2], θ[3]]
```

The exact formatting may depend on the Qiskit version.

### Assigning parameter values

```python
parameter_values = [3.14, 1.57, 0.50, 2.00]
bound_circuit = circuit.assign_parameters(parameter_values)
```

This replaces the symbolic parameters with numerical values.

For example:

```text
θ[0] → 3.14
θ[1] → 1.57
θ[2] → 0.50
θ[3] → 2.00
```

After this step, the circuit is no longer symbolic; it has concrete rotation angles.

### Decomposing the circuit

```python
print(bound_circuit.decompose())
```

This prints the actual lower-level gates used in the ansatz. Instead of seeing one high-level block, the learner sees gates such as `Ry` and `CX`.

## Quantum meaning

The ansatz prepares a trial quantum state. The rotation gates change the qubit states, while the entangling gate creates correlations between the qubits.

The parameters control the shape of the quantum state. Changing the angles changes the state prepared by the circuit.

In variational algorithms, a classical optimizer repeatedly changes the angles until the circuit gives the best result for a chosen objective function.

## Expected output

The code should print:

```text
Parameters: [ParameterVectorElement(θ[0]), ParameterVectorElement(θ[1]), ...]
```

and a decomposed circuit containing gates similar to:

```text
Ry(3.14)
Ry(1.57)
CX
Ry(0.5)
Ry(2)
```

The exact printed diagram may vary slightly depending on the Qiskit version.

## Warning observed during testing

During testing, Qiskit produced a deprecation warning:

```text
RealAmplitudes is deprecated as of Qiskit 2.1 and will be removed in Qiskit 3.0.
Use the function qiskit.circuit.library.real_amplitudes instead.
```

This warning does **not** mean the example failed. It means the current code still runs, but it should eventually be updated to the newer Qiskit syntax.

## Safe modifications

Beginners can safely modify:

### 1. Parameter values

```python
parameter_values = [0.0, 0.5, 1.0, 1.5]
```

This changes the rotation angles and therefore changes the final quantum state.

### 2. Number of repetitions

```python
circuit = RealAmplitudes(num_qubits=2, entanglement="linear", reps=2)
```

This makes the circuit deeper and adds more parameters. It may make the ansatz more expressive, but it also makes it more complex.

### 3. Number of qubits

```python
circuit = RealAmplitudes(num_qubits=3, entanglement="linear", reps=1)
```

This increases the size of the circuit. More qubits usually means more parameters and more entangling operations.

### 4. Entanglement pattern

```python
circuit = RealAmplitudes(num_qubits=3, entanglement="full", reps=1)
```

This changes how qubits are connected by entangling gates.

## Unsafe or confusing modifications

Avoid changing the number of parameter values without checking the number of parameters.

For example, if the circuit has four parameters, this may fail:

```python
parameter_values = [3.14, 1.57]
```

The circuit expects one value for each parameter.

Also avoid assuming that the order of parameters is obvious without checking:

```python
params = list(circuit.parameters)
```

Always inspect the parameter list before binding values.

## Questions for line-by-line study

1. What is an ansatz?
2. Why do we use parameters instead of fixed rotation angles?
3. What is the difference between a symbolic circuit and a bound circuit?
4. What does `assign_parameters()` do?
5. Why do variational algorithms need both a quantum circuit and a classical optimizer?
6. What happens when `reps` is increased?
7. Why can deeper circuits become more sensitive to hardware noise?

## How this fits into the learning path

```text
basic gates
→ Bell states
→ Sampler and Estimator
→ parameterized ansatz circuits
→ VQE and QAOA
→ chemistry, materials, and optimization applications
```

This example is the learner's first step toward understanding hybrid quantum-classical algorithms.
