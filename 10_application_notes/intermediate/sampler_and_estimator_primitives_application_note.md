# Application Note: Sampler and Estimator Primitives

## Application level

Intermediate.

## Core idea

Quantum circuits do not become useful simply because they are drawn. They become computational tools when we use them to generate numerical outputs. Qiskit primitives provide this bridge.

```text
Sampler -> measurement outcomes and distributions
Estimator -> expectation values of observables
```

## Why this matters for applications

Many quantum computing applications require repeated evaluation of circuits.

Examples:

- sampling output distributions
- estimating energy
- estimating correlations
- comparing simulator and hardware behavior
- evaluating optimization candidates
- building hybrid quantum-classical algorithms

## Application areas

### 1. Quantum simulation

Estimator-style workflows allow learners to compute quantities such as:

```text
<Z>
<ZZ>
<Hamiltonian>
```

This is a first step toward simulation of molecules, materials, spin models, and condensed-matter systems.

### 2. Optimization

Many quantum optimization workflows repeatedly run circuits and evaluate objective functions. The Sampler provides the distribution of candidate bit strings. The best bit strings may correspond to good solutions of a problem.

Examples include:

- graph partitioning
- MaxCut
- scheduling
- routing
- resource allocation

### 3. Hardware comparison

The same circuit can be run on an ideal simulator and on real hardware. Differences between ideal and hardware outcomes reveal noise, calibration limits, and measurement errors.

This supports beginner research questions such as:

```text
How close is the real device to the ideal simulator?
Which outputs are expected?
Which outputs are noise?
How does the number of shots affect the result?
```

### 4. STEM education

Primitives help students move from diagrams to data. Students can see that a circuit produces a measurable statistical pattern.

This is useful for teaching:

- probability
- binary outcomes
- uncertainty
- correlation
- expectation values
- model-versus-data thinking

## Connection to the code library

This application note connects to:

```text
03_primitives/statevector_sampler_current_version.py
03_primitives/sampler_examples.py
03_primitives/estimator_zz_expectation.py
02_bell_states/bell_state_sampler.py
07_algorithms_intro/vqe_intro.ipynb
```

The logical pathway is:

```text
Measurement counts -> Sampler -> Correlations -> Estimator -> Hamiltonian energy -> VQE
```

## Limits and cautions

Sampler output is statistical. A finite number of shots always produces fluctuations.

Estimator output depends on the chosen observable. If the observable does not match the circuit or has the wrong number of qubits, the code will fail or become meaningless.

Real hardware output includes noise. Therefore, simulator results and hardware results should not be expected to match perfectly.

## Beginner research questions

1. How does the number of shots change the stability of the result?
2. How do simulator counts compare with hardware counts?
3. What observable should be used to detect Bell-state correlation?
4. What is the connection between `<ZZ>` and physical correlation?
5. How does Estimator output become an energy in VQE?
