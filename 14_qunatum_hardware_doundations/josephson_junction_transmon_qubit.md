# Josephson Junction / Transmon Qubit

A Josephson-junction qubit is a superconducting circuit whose quantum behavior is made possible by a nonlinear circuit element: the Josephson junction.

## Why the Josephson junction matters

An ordinary LC oscillator has evenly spaced energy levels. Even spacing is a problem because a drive resonant with one transition can also excite other transitions.

A Josephson junction adds nonlinearity. This makes the energy levels unevenly spaced, allowing the two lowest levels to be isolated as a qubit.

```text
|0> = ground state of the nonlinear circuit
|1> = first excited state of the nonlinear circuit
```

## Transmon idea

A transmon is a Josephson junction shunted by a capacitor. The large shunt capacitance reduces sensitivity to charge noise while preserving enough nonlinearity to define a qubit.

## Simplified circuit elements

| Element | Role |
|---|---|
| Josephson junction | Provides nonlinear inductance and quantum nonlinearity |
| Shunt capacitor | Reduces charge noise sensitivity |
| Microwave drive line | Applies single-qubit control pulses |
| Readout resonator | Allows state measurement |
| Coupling element | Enables qubit-qubit interaction or coupling to resonator |
| Cryogenic environment | Suppresses thermal excitations and decoherence |

## Hardware-to-gate connection

Single-qubit gates are implemented by shaped microwave pulses. For example:

```text
microwave pulse with calibrated amplitude and phase -> RX, RY, RZ-like rotations
```

Two-qubit gates are implemented by controlled interactions between neighboring qubits or via resonator-mediated coupling.

## Measurement

A transmon is often read out dispersively through a resonator. The qubit state shifts the resonator response, and classical electronics infer whether the measurement result is closer to 0 or 1.

## Student message

The abstract circuit line in a Qiskit diagram corresponds to a physical superconducting device controlled by microwave pulses and measured by classical electronics.
