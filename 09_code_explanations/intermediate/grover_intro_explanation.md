# Grover Intro Teaching Unit

## Code file

`07_algorithms_intro/grover_intro.py`

## Level

Intermediate.

## Purpose

This teaching unit explains a small Grover-search example. The code demonstrates how a quantum circuit can mark one target state and amplify its measurement probability.

In the tested run, the target state was:

```text
11
```

The output was:

```text
Counts: {'11': 1000}
```

This means the circuit successfully amplified the target state in an ideal simulator.

## Main idea

Grover search is a quantum algorithm for finding a marked item in an unstructured search space. For a two-qubit system, the possible computational-basis states are:

```text
00, 01, 10, 11
```

The example marks the state `11` and then applies an amplification step so that measurement returns `11` with high probability.

## How this fits in the learning pathway

```text
Hadamard superposition
→ many possible basis states
→ oracle marks a target state
→ diffusion/amplification increases target probability
→ measurement reveals the target
```

This makes Grover a bridge between basic superposition and application-oriented quantum algorithms.

## Concepts introduced

- superposition
- oracle
- marked state
- amplitude amplification
- measurement counts
- search space
- probability amplification

## Typical circuit logic

A small Grover circuit usually contains the following conceptual blocks:

```text
1. Prepare equal superposition with Hadamard gates.
2. Apply an oracle that marks the target state.
3. Apply a diffusion operator that amplifies the marked state.
4. Measure the qubits.
```

## Line-by-line study questions

Use these questions when reading `grover_intro.py`:

1. Where are the qubits placed into superposition?
2. Which lines mark the target state?
3. Which lines act as the diffusion/amplification step?
4. Where are the qubits measured?
5. Why should `11` dominate the final counts?
6. What changes if the target state is changed?

## Safe modifications

Beginner-safe modifications include:

```text
1. Change the number of shots.
2. Change the target state if the oracle is rewritten carefully.
3. Print the circuit before and after the oracle block.
4. Add comments labeling the superposition, oracle, diffusion, and measurement sections.
```

## Modifications that need caution

Do not casually change the oracle or diffusion gates without predicting the effect. The circuit may still run, but it may no longer implement Grover search correctly.

Common mistakes include:

```text
- marking the wrong state
- applying the diffusion operator incorrectly
- measuring before amplification
- changing qubit order without updating interpretation
```

## Expected output

For the tested example, the target state is `11`, so the expected output is:

```text
Counts: {'11': 1000}
```

Small variations can occur depending on the simulator and shot count, but the marked state should dominate.

## Why this example matters

Grover search is one of the classic examples showing that quantum algorithms can change the scaling of a problem. It does not solve every search problem automatically, and present-day hardware limits large demonstrations, but it is a foundational algorithm for learning how quantum interference can be engineered to make desired answers more likely.

## Connection to later topics

Grover connects to:

- oracle design
- amplitude amplification
- constraint satisfaction
- optimization
- database search concepts
- quantum speedup analysis
- algorithmic thinking beyond simple circuits

## Beginner summary

This code teaches a new idea: quantum circuits can be designed so that the wrong answers interfere away while the desired answer becomes more likely. Grover search is therefore not just about measurement. It is about building a circuit that reshapes probability before measurement.
