# Classical-Quantum Hybrid Architecture

Quantum computers are not purely quantum machines. They rely heavily on classical computers and electronics.

## Workflow

```text
algorithm
-> circuit
-> transpilation
-> pulse schedule
-> hardware execution
-> measurement
-> classical processing
-> possible feedback
```

## Why classical hardware is essential

Classical systems:

- compile algorithms
- generate control pulses
- time the pulses
- acquire readout signals
- decode measurement results
- update variational parameters
- perform error correction decoding

## Student message

A quantum processor is a special-purpose quantum device embedded inside a much larger classical control system.
