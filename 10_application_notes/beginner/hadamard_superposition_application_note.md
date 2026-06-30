# Application Note — Hadamard Superposition

**Related code:** `01_basic_circuits/hadamard_superposition.py`  
**Level:** Beginner  
**Application family:** quantum sampling, measurement, probability, and algorithm initialization

## Why this example is useful

The Hadamard superposition example is a small code, but it introduces a central feature of quantum computing: a circuit can prepare a state whose measurement produces a probability distribution.

This is the first step toward understanding why quantum computing is not just classical programming with different syntax.

## Natural problem type

This example connects to problems involving:

```text
probability
sampling
randomness
interference
state preparation
measurement statistics
```

Many larger quantum algorithms begin by applying Hadamard gates to create a uniform superposition over many possible states.

## Basic application connection

A single Hadamard gate can be used to demonstrate quantum random-bit generation in an idealized educational setting.

The circuit:

```text
|0> → H → measurement
```

produces outcomes approximately distributed as:

```text
0 with probability 1/2
1 with probability 1/2
```

## Intermediate application connection

Hadamard gates are used to create search spaces and interference patterns. They appear in:

```text
Bell-state preparation
Grover search
Deutsch-Jozsa algorithm
Quantum Fourier Transform
phase estimation
many initialization circuits
```

## Advanced application connection

In advanced algorithms, Hadamard gates are not the final goal. They are part of larger structures that allow quantum amplitudes to interfere. This interference is what allows some quantum algorithms to amplify useful answers and suppress unwanted answers.

Examples include:

```text
search and amplitude amplification
period finding
phase estimation
optimization algorithms
Hamiltonian simulation workflows
```

## Limitation

The Hadamard example alone does not demonstrate quantum advantage. It is a foundation code. Its purpose is to teach the learner how superposition, measurement, shots, and counts work before moving to multi-qubit circuits and algorithms.

## Student reflection question

If the Hadamard gate creates a 50/50 measurement result for one qubit, what happens when Hadamard gates are applied to two, three, or many qubits?
