# Quantum Control and Measurement

Quantum gates are implemented by control signals applied to physical qubits.

## Single-qubit gates

For a superconducting qubit, a microwave pulse with calibrated amplitude, duration, frequency, and phase can implement rotations such as:

```text
RX(theta), RY(theta), RZ(phi)
```

## Two-qubit gates

Two-qubit gates require an interaction between qubits. Examples include:

```text
CZ, CNOT, iSWAP, RXX, RYY, RZZ
```

The physical mechanism depends on the hardware platform.

## Measurement

Measurement converts a quantum state into a classical bit. In real experiments this usually requires:

```text
physical readout signal -> amplifier -> digitizer -> thresholding -> classical bit
```

## Shots

A quantum circuit is often repeated many times. Each repetition is called a shot. The output is a distribution of bitstrings, not a single deterministic answer.
