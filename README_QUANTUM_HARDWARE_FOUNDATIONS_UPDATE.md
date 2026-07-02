# Quantum Hardware Foundations Update

This is a **partial update** for `qc-code-study-library`.

It adds a new student-facing documentation track:

```text
14_quantum_hardware_foundations/
```

The purpose is to connect gate-based quantum computing with the physical hardware that makes it possible. The module emphasizes Josephson-junction / transmon qubits as the first detailed example, while also comparing superconducting, trapped-ion, photonic, spin, and neutral-atom platforms.

## Added documentation

```text
14_quantum_hardware_foundations/
├── README.md
├── transistor_vs_qubit_computing.md
├── quantum_hardware_stack.md
├── josephson_junction_transmon_qubit.md
├── superconducting_qubits.md
├── trapped_ion_qubits.md
├── photonic_qubits.md
├── spin_qubits.md
├── neutral_atom_qubits.md
├── quantum_control_and_measurement.md
├── classical_quantum_hybrid_architecture.md
├── hardware_to_gate_mapping_table.md
└── student_reflection_questions.md
```

## Added code templates

```text
12_advanced_codes/quantum_hardware_foundations/
├── transistor_vs_qubit_logic_diagram.py
├── josephson_transmon_energy_levels.py
├── qubit_control_pulse_visualization.py
├── bloch_sphere_gate_sequence.py
├── measurement_shots_histogram.py
└── classical_quantum_hybrid_workflow.py
```

## Recommended run order

```bat
python 12_advanced_codes\quantum_hardware_foundations\transistor_vs_qubit_logic_diagram.py
python 12_advanced_codes\quantum_hardware_foundations\josephson_transmon_energy_levels.py
python 12_advanced_codes\quantum_hardware_foundations\qubit_control_pulse_visualization.py
python 12_advanced_codes\quantum_hardware_foundations\bloch_sphere_gate_sequence.py
python 12_advanced_codes\quantum_hardware_foundations\measurement_shots_histogram.py
python 12_advanced_codes\quantum_hardware_foundations\classical_quantum_hybrid_workflow.py
```
