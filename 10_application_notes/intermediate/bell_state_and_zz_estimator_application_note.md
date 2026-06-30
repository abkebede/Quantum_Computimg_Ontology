# Application Note — Bell States, Correlations, and the ZZ Estimator

## Code files

- `02_bell_states/bell_state_sampler.py`
- `03_primitives/estimator_zz_expectation.py`

## Why this example matters

The Bell-state example is the first point in the library where a learner sees a genuinely quantum relationship between two qubits. A single-qubit Hadamard circuit teaches superposition and probability. A Bell-state circuit teaches entanglement and correlation.

The `ZZ` Estimator example then goes one step further. It shows that quantum circuits are not only used to produce measurement counts. They can also be used to evaluate physical and mathematical quantities called expectation values.

## Problem type

This example belongs to the problem type:

```text
correlation measurement
observable evaluation
quantum information
foundation for Hamiltonian measurement
```

## Classical comparison

In classical computing, two bits can be correlated because they were copied or assigned together. In quantum computing, two qubits can be correlated through entanglement. The Bell state creates a state where the two-qubit system must be treated as one joint quantum state.

## Quantum-computing concept

The Bell state is:

```text
(|00> + |11>) / sqrt(2)
```

This means the system is not simply qubit 0 having one state and qubit 1 having another independent state. The two qubits are correlated as a pair.

## Observable connection

The observable `ZZ` measures correlation in the Z basis.

For the Bell state:

```text
<ZZ> = +1
```

This is important because many quantum algorithms and quantum simulations are based on measuring expectation values of Pauli operators and Hamiltonians.

## Applications that build from this idea

### 1. Quantum communication

Bell states are used as conceptual building blocks for quantum teleportation, superdense coding, and entanglement-based communication protocols.

### 2. Quantum networking

Quantum networks require the creation, distribution, and verification of entanglement between separated quantum systems.

### 3. Quantum simulation

In many-body physics, one often measures correlations between sites or spins. A simple `ZZ` measurement is the smallest version of this idea.

### 4. Materials and condensed-matter physics

Spin models, magnetic correlations, and lattice Hamiltonians often contain terms such as `ZZ`, `XX`, and `YY`. The two-qubit Estimator example introduces the same mathematical structure in its simplest form.

### 5. Quantum algorithms

Variational algorithms such as VQE and QAOA use observables and Hamiltonians built from Pauli terms. The `ZZ` Estimator example is a first step toward those applications.

## Beginner limitation

This example does not solve a large real-world problem by itself. Its value is foundational. It teaches the learner how quantum correlations are created, measured, and represented in code.

## How this fits into the learning sequence

```text
Hadamard superposition
→ Bell-state entanglement
→ ZZ expectation value
→ Hamiltonian expectation values
→ VQE and QAOA
→ quantum chemistry, materials, optimization, and many-body physics
```

## Suggested student exercise

Run the Bell-state sampler code and record the counts. Then run the Estimator code and record `<ZZ>`. Explain why the Sampler gives a count dictionary while the Estimator gives a number.

Then modify the observable from `ZZ` to `XX` and predict whether the Bell state is still correlated in that basis.
