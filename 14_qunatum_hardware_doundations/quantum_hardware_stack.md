# Quantum Hardware Stack

Quantum computing requires many layers working together.

## Layer 1: Physical quantum system

Examples include superconducting circuits, trapped ions, neutral atoms, photons, electron spins, and nuclear spins.

## Layer 2: Qubit encoding

A qubit requires two states chosen from the physical system.

Examples:

```text
superconducting qubit: two lowest energy levels of a nonlinear circuit
trapped ion: two internal atomic states
photon: polarization or path modes
spin qubit: spin-up and spin-down states
neutral atom: two hyperfine or Rydberg-related states
```

## Layer 3: Control

The system must be controlled by microwave pulses, laser pulses, magnetic fields, electric fields, or voltage gates.

## Layer 4: Quantum gates

Control signals implement operations such as:

```text
X, Y, Z, H, RX, RY, RZ, CNOT, CZ, RXX, RYY, RZZ
```

## Layer 5: Measurement

The final quantum state must be converted into a classical measurement result.

## Layer 6: Classical electronics

Classical electronics generate pulses, acquire signals, demodulate readout, threshold measurements, and run feedback.

## Layer 7: Software

Software such as Qiskit compiles circuits into backend instructions. These instructions are ultimately translated into hardware-level operations.

## Core message

Quantum computing is a hybrid architecture:

```text
classical software + classical control hardware + quantum processor + classical measurement processing
```
