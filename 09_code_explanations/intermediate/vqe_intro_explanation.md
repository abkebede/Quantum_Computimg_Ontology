# VQE Intro Teaching Unit: Hamiltonians, Ansatz Circuits, and Energy Minimization

**Level:** Intermediate to advanced beginner  
**Primary file:** `07_algorithms_intro/vqe_intro.ipynb`  
**Main idea:** Use a parameterized quantum circuit and an estimator to minimize the energy of a small Hamiltonian.

## 1. Why this example matters

The VQE example is one of the first examples in the library that connects quantum code to a recognizable scientific problem: estimating the energy of a quantum system. It moves beyond gate demonstrations and shows how quantum computing can be used as part of a hybrid quantum-classical workflow.

The basic structure is:

```text
Hamiltonian + ansatz + estimator + classical optimizer = VQE
```

This is important for quantum chemistry, materials science, condensed-matter physics, and energy-related simulation problems.

## 2. What VQE means

**VQE** stands for **Variational Quantum Eigensolver**.

It is called **variational** because the circuit has adjustable parameters. The algorithm changes these parameters to lower the measured energy.

It is called an **eigensolver** because the goal is to approximate the lowest eigenvalue of a Hamiltonian. In physics, the lowest eigenvalue of a Hamiltonian is the ground-state energy.

## 3. Main ingredients

### Hamiltonian

The Hamiltonian represents the energy operator of the system. In this teaching notebook, the Hamiltonian is written as a sum of Pauli terms:

```text
H = c0 II + c1 IZ + c2 ZI + c3 ZZ + c4 XX
```

Each term has:

```text
Pauli string + numerical coefficient
```

For example:

```python
("ZZ", -0.01128010425623538)
```

means a `ZZ` observable with that coefficient.

### Ansatz

An **ansatz** is a parameterized trial circuit. It prepares a family of possible quantum states. The optimizer searches through this family by changing the parameters.

A typical ansatz contains:

```text
rotation gates + entangling gates + adjustable parameters
```

### Estimator

The estimator computes an expectation value:

```text
<psi(theta)|H|psi(theta)>
```

In beginner language, it answers:

```text
For this trial quantum state, what is the average energy?
```

### Classical optimizer

The optimizer changes the circuit parameters and tries to make the energy smaller.

## 4. How the notebook fits into the learning pathway

This notebook depends on earlier ideas:

```text
Hadamard superposition
→ Bell states
→ measurement counts
→ Estimator <ZZ>
→ parameterized circuits
→ Hamiltonian expectation value
→ VQE energy minimization
```

So VQE is not an isolated code. It is the point where several earlier concepts come together.

## 5. Line-by-line study guide

When reviewing the notebook, ask these questions.

### Imports

Look for imports such as:

```python
from qiskit.circuit.library import RealAmplitudes
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator
from scipy.optimize import minimize
```

Ask:

```text
What object is being imported?
Is it a Qiskit circuit object, a quantum information object, a primitive, or a classical optimizer?
```

### Hamiltonian construction

When you see:

```python
SparsePauliOp.from_list([...])
```

ask:

```text
How many qubits does each Pauli string act on?
What physical quantity is represented?
Which terms represent single-qubit effects?
Which terms represent two-qubit correlations?
```

### Ansatz construction

When you see the ansatz circuit, ask:

```text
How many qubits does it use?
How many parameters does it have?
Which gates are parameterized?
Which gates entangle qubits?
```

### Energy function

The energy function is the center of the algorithm. It takes a parameter vector, assigns it to the circuit, evaluates the Hamiltonian expectation value, and returns a number.

Ask:

```text
What does the function receive?
What circuit state does it prepare?
What observable does it evaluate?
What number does it return?
```

### Optimizer

When the optimizer runs, ask:

```text
What initial parameter values were chosen?
How many iterations were allowed?
What minimum energy was found?
What parameter values produced that energy?
```

## 6. Expected result

In the tested repository workflow, the VQE notebook ran successfully and produced a minimum energy near:

```text
-1.857
```

The exact value may vary slightly depending on optimizer settings and package versions.

## 7. Safe modifications

Beginners can safely modify:

```text
initial parameter values
optimizer maximum iterations
ansatz repetitions
ansatz entanglement pattern
Hamiltonian coefficients in small test cases
```

Each modification should be done one line at a time.

## 8. Unsafe or advanced modifications

Do not casually modify:

```text
number of qubits without updating the Hamiltonian
Pauli strings without checking their length
estimator input format
optimizer function signature
measured vs unmeasured circuits
```

For example, a two-qubit circuit requires two-character Pauli strings such as `ZZ`, `ZI`, `IZ`, or `XX`. A string such as `ZZZ` belongs to a three-qubit problem and will not match a two-qubit ansatz.

## 9. Beginner questions

1. What is the difference between measuring counts and estimating an expectation value?
2. Why does VQE need a Hamiltonian?
3. What is an ansatz?
4. Why does the optimizer run many times?
5. What does the minimum energy mean physically?
6. Why is VQE called a hybrid quantum-classical algorithm?
7. What happens if we increase the number of ansatz repetitions?
8. What kinds of real scientific problems can be represented by Hamiltonians?

## 10. Summary

This example is the first major application-oriented teaching unit in the repository. It shows how quantum circuits can be used to represent trial states and how expectation values can connect quantum circuits to physical energy problems.

For beginners, the important lesson is not only the final number. The important lesson is the workflow:

```text
Build a Hamiltonian
Build a parameterized circuit
Evaluate energy
Change parameters
Search for the lowest energy
Interpret the result
```
