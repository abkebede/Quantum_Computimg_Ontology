# Advanced Code Status Table

This table tracks the advanced quantum-computing code families in `qc-code-study-library`.

Use the table to distinguish between:

- **Working example**: intended to run directly in the current Qiskit environment.
- **Concept template**: pedagogical or structural code that explains the method but may need adaptation before execution.
- **Needs test**: file is present but has not yet been verified locally.
- **Needs API review**: code may depend on Qiskit syntax that changes between versions.
- **Needs expansion**: basic example exists, but the scientific or algorithmic content needs deeper treatment.

## Master advanced status table

| Area | Topic | Example file | Current status | Tested? | Application connection | Next improvement |
|---|---|---|---|---|---|---|
| Optimization | Simple QAOA / MaxCut | `07_algorithms_intro/qaoa_maxcut_intro.py` | Working-example candidate | Needs test | Graph partitioning, scheduling, routing, logistics | Add graph drawing, cost-history plot, and line-by-line teaching note |
| Optimization | QAOA penalty Hamiltonian | `12_advanced_codes/optimization/qaoa_penalty_hamiltonian_template.py` | Concept template | Needs test/review | constrained optimization, resource allocation | Add executable example with explicit binary constraint |
| Chemistry | Small molecular Hamiltonian / VQE | `12_advanced_codes/chemistry/h2_hamiltonian_vqe_grid_search.py` | Working-example candidate | Needs test | molecular ground-state energy, catalysis, chemistry education | Add molecular interpretation and comparison to exact diagonalization |
| Materials | Transverse-field Ising chain | `12_advanced_codes/materials/transverse_field_ising_chain.py` | Working-example candidate | Needs test | magnetism, quantum phase transitions, many-body physics | Add parameter sweep over field strength |
| Materials | Heisenberg spin chain | `12_advanced_codes/materials/heisenberg_spin_chain_hamiltonian.py` | Working-example candidate | Needs test | magnetic materials, spin correlations | Add ground-state energy comparison for small chains |
| Materials | Hubbard model | `12_advanced_codes/materials/hubbard_model_two_site_simplified.py` | Concept model | Needs review | correlated electrons, superconductivity, Mott physics | Add fermion-to-qubit mapping explanation |
| Algorithms | Phase estimation | `07_algorithms_intro/phase_estimation_intro.py` | Working-example candidate | Needs test | energy estimation, spectra, Shor-type algorithms | Add inverse-QFT explanation and phase-to-eigenvalue interpretation |
| Algorithms | Amplitude estimation | `07_algorithms_intro/amplitude_estimation_intro.py` | Concept/working candidate | Needs test | Monte Carlo, probability estimation, risk analysis | Clarify whether it is true QAE or pedagogical probability-estimation template |
| Monte Carlo | Amplitude-estimation application | `12_advanced_codes/monte_carlo_sampling/amplitude_estimation_application_template.py` | Concept template | Needs review | risk, finance, environmental sampling, uncertainty quantification | Add concrete probability model |
| QML | Quantum kernel | `12_advanced_codes/qml/quantum_kernel_intro.py` | Working-example candidate | Needs test | materials/spectroscopy pattern recognition | Add classical-kernel comparison and small dataset |
| Error mitigation | Readout mitigation | `12_advanced_codes/error_mitigation/readout_mitigation_intro.py` | Working-example candidate | Needs test | hardware-aware quantum computing | Add confusion matrix and corrected counts |
| Error correction | Bit-flip repetition code | `12_advanced_codes/error_correction/bit_flip_repetition_code.py` | Working-example candidate | Needs test | error correction fundamentals | Add syndrome measurement explanation |
| Hardware noise | Noisy simulator study | `03_primitives/noisy_simulator_bell_comparison.py` and `12_advanced_codes/hardware_noise/simulator_noise_study_template.py` | Partial / template | Needs test | simulator vs noisy simulator vs hardware | Add common noise channels and comparison plots |
| IBM hardware | Simulator vs hardware Bell | `05_ibm_hardware/simulator_vs_hardware_bell_comparison_template.py` | Token-safe hardware template | Requires IBM account | real backend execution, calibration awareness | Add result import/export and post-run report form |
| Linear algebra | HHL concept | `12_advanced_codes/linear_algebra/hhl_linear_system_concept.py` | Concept template | Needs review | linear systems, PDEs, engineering models | Add small 2x2 matrix example and explain limitations |
| Cryptography | Shor period-finding concept | `12_advanced_codes/cryptography/shor_period_finding_concept.py` | Concept template | Needs review | period finding, factoring, cryptography education | Keep educational; avoid misleading claims about practical factoring |
| Quantum simulation | Trotterized Ising time evolution | `12_advanced_codes/quantum_simulation/trotterized_ising_time_evolution.py` | Working-example candidate | Needs test | dynamics, time evolution, many-body simulation | Add observable vs time plot |
| OpenQASM | Cuccaro ripple-carry adder | `06_openqasm_examples/cuccaro_ripple_carry_adder.qasm` | Source-study example | Source reviewed, runner needed | reversible arithmetic, arithmetic circuits | Add OpenQASM 3 runner or documented execution workflow |

## Status legend

| Status | Meaning |
|---|---|
| Working-example candidate | The file is intended to run but still needs local verification. |
| Working example | The file has been run successfully and output has been recorded. |
| Concept template | The file is pedagogical and may require adaptation before execution. |
| Source-study example | The file is useful for reading and analysis even if no runner is included yet. |
| Needs API review | The code may require syntax updates for the current Qiskit version. |
| Requires IBM account | Cannot be fully tested without a token-safe IBM Quantum account setup. |

## Testing record template

Copy this block under the relevant file after testing.

```markdown
### Test record: <file path>

- Date tested:
- Tester:
- Operating system:
- Python executable:
- Python version:
- Qiskit version:
- Command used:
- Result: Passed / Failed / Partial
- Output summary:
- Warnings:
- Errors:
- Notes:
```
