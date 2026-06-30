# Application Note — Parameterized Ansatz Circuits

## Code connection

```text
04_parameterized_circuits/real_amplitudes_ansatz.py
```

## Main idea

A parameterized ansatz circuit is a tunable quantum model. It has a fixed gate structure, but some gates contain adjustable angles.

This makes the circuit useful for hybrid quantum-classical algorithms, where a classical optimizer changes the parameters and a quantum circuit evaluates the result.

## Application areas

### 1. Quantum chemistry

In VQE, an ansatz prepares trial molecular states. The optimizer changes the circuit parameters to minimize the molecular energy.

This connects to problems such as:

```text
molecular ground-state energy
reaction pathways
catalysis
hydrogen chemistry
small molecular Hamiltonians
```

### 2. Materials modeling

Parameterized circuits can represent trial states for model Hamiltonians used in materials physics.

Examples include:

```text
spin models
strongly correlated materials
superconductivity models
transition-metal oxide models
lattice Hamiltonians
```

### 3. Optimization

Parameterized circuits are used in QAOA and related hybrid methods for optimization problems.

Examples include:

```text
MaxCut
scheduling
resource allocation
routing
portfolio-style optimization
energy-grid optimization
```

### 4. Quantum machine learning

Parameterized circuits can be used as trainable quantum models.

Examples include:

```text
quantum classifiers
quantum kernels
feature maps
hybrid neural-network-like models
```

## Why this matters for beginners

The beginner first learns gates as fixed operations:

```text
X, H, CX, measure
```

Parameterized circuits introduce a new idea:

```text
a gate can contain a variable angle
```

That idea is essential for algorithms that learn, optimize, or approximate physical systems.

## Limits and cautions

Parameterized circuits are powerful, but they are not magic. Practical performance depends on:

```text
ansatz choice
number of parameters
optimizer behavior
noise
circuit depth
hardware connectivity
problem encoding
```

A deeper circuit may be more expressive, but on real quantum hardware it may also accumulate more error.

## Learning goal

After studying this example, a learner should understand:

```text
A parameterized circuit is a tunable quantum circuit.
The parameters control the output state.
Variational algorithms use these parameters to minimize or optimize a quantity.
```
