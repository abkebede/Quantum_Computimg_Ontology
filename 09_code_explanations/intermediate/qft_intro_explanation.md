# QFT Intro — Line-by-Line Teaching Unit

## Code title

Quantum Fourier Transform Intro

## File

```text
07_algorithms_intro/qft_intro.py
```

## Level

Intermediate

## Purpose

This code introduces the Quantum Fourier Transform, usually abbreviated as QFT. The QFT is the quantum-circuit version of a Fourier transform. It changes a computational-basis state into a phase-encoded superposition. It is a central building block in advanced quantum algorithms.

## What the code demonstrates

The example constructs a three-qubit QFT circuit. It prepares an input state using an `X` gate and then applies the standard QFT pattern:

```text
Hadamard gates
controlled phase rotations
final qubit swaps
```

The output of the code is a circuit diagram, not measurement counts. The purpose is to help the learner see the structure of the QFT circuit.

## Quantum idea

Classical Fourier analysis rewrites a signal in terms of frequencies. The QFT rewrites quantum amplitudes in terms of phase relationships. This is why QFT is important in algorithms that extract periodicity or phase information.

## Important gates

### X gate

The `X` gate flips a qubit:

```text
|0> -> |1>
|1> -> |0>
```

In the example, an `X` gate is used to prepare a nonzero input state.

### H gate

The Hadamard gate creates superposition. In QFT, Hadamard gates begin the process of spreading amplitude information across basis states.

### Controlled phase gate

Controlled phase gates apply a phase rotation to one qubit depending on the state of another qubit. These gates are what encode Fourier phase structure.

### Swap gate

The QFT circuit often ends with swap gates to reverse the order of qubits. This is necessary because the QFT naturally produces the output in reversed bit order.

## Qiskit syntax to notice

Typical QFT example code may include patterns such as:

```python
qc = QuantumCircuit(3)
qc.x(0)
qc.h(0)
qc.cp(pi/2, 1, 0)
qc.cp(pi/4, 2, 0)
qc.swap(0, 2)
print(qc.draw())
```

The exact implementation may vary, but the syntax usually uses:

```text
QuantumCircuit
x
h
cp
swap
draw
```

## Line-by-line study questions

For each line in the QFT code, ask:

```text
What qubit does this line act on?
Does this line create superposition, phase, or reordering?
Is this line preparing the input or applying the QFT?
What happens if this line is removed?
What happens if the phase angle is changed?
```

## Safe modifications

The beginner-safe modifications are:

```text
1. Move the initial X gate to a different qubit.
2. Add another X gate to prepare a different basis input.
3. Change the number of qubits only after understanding the QFT pattern.
4. Print the circuit using different drawing methods.
```

Example:

```python
qc.x(0)
```

can be changed to:

```python
qc.x(1)
```

This changes the input state before QFT is applied.

## Modifications requiring caution

Be careful modifying:

```text
controlled phase angles
order of controlled phase gates
final swap operations
number of qubits
```

These lines define the mathematical structure of the QFT. Changing them may produce a circuit that still runs but is no longer the true QFT.

## Expected output

The expected output is a three-qubit circuit diagram showing:

```text
initial input preparation
Hadamard gates
controlled phase gates
final swaps
```

The code is successful if the circuit prints without error and shows the QFT structure.

## Why this code matters

This example is a bridge from simple circuits to advanced quantum algorithms. QFT is a key component of:

```text
phase estimation
period finding
Shor-type algorithms
quantum signal processing
Hamiltonian simulation methods
```

## Application connection

QFT itself is not usually the final application. It is a subroutine. It becomes powerful when embedded inside algorithms that need phase or periodicity information.

Examples include:

```text
estimating eigenvalues
finding periods
analyzing quantum phases
supporting algorithms for number theory
supporting simulation algorithms
```

## Beginner interpretation

A beginner can think of the QFT as the quantum version of changing from a position/basis description to a phase/frequency description. This is similar in spirit to how Fourier analysis in physics changes a function from time or space into frequency or wave-number components.

## Status in the tested repository

The QFT example was tested in the `qgss_env` environment and printed the expected circuit diagram successfully.

```text
Status: Passed
File: 07_algorithms_intro/qft_intro.py
Result: 3-qubit QFT circuit printed successfully
```
