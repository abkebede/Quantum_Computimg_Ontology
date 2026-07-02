# Quantum Hardware Foundations

A quantum circuit is not only a mathematical diagram. It is an instruction sequence for a real physical quantum device.

This module explains how gate-based quantum computing emerges from hardware. It starts with the comparison between transistor-based classical computation and qubit-based quantum computation, then builds a layered view of the quantum hardware stack.

## Core idea

Classical digital computing uses engineered switching devices:

```text
voltage -> transistor state -> logic gate -> circuit -> computation
```

Quantum computing uses engineered controllable quantum systems:

```text
control pulse -> qubit state -> quantum gate -> quantum circuit -> measurement
```

## Recommended path

1. Read `transistor_vs_qubit_computing.md`.
2. Read `quantum_hardware_stack.md`.
3. Study `josephson_junction_transmon_qubit.md` as the first detailed hardware example.
4. Compare hardware platforms using the platform-specific notes.
5. Run the supporting visualization scripts in `12_advanced_codes/quantum_hardware_foundations/`.
