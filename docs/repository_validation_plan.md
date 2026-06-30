# Repository Validation Plan

The purpose of validation is to move the project from a collection of files into a tested, teachable, contributor-ready quantum-computing code library.

## Validation phases

### Phase 1 — Structure validation

Check that the repository contains the expected directories:

```text
00_environment_test/
01_basic_circuits/
02_bell_states/
03_primitives/
04_parameterized_circuits/
05_ibm_hardware/
06_openqasm_examples/
07_algorithms_intro/
08_applications_by_problem_type/
09_code_explanations/
10_application_notes/
11_problem_to_algorithm_maps/
12_advanced_codes/
docs/
ontology/
setup_guides/
```

### Phase 2 — Environment validation

Run:

```bat
python 00_environment_test\environment_check.py
```

Record:

- Python executable;
- Python version;
- Qiskit version;
- qiskit-aer version;
- qiskit-ibm-runtime version;
- qiskit-algorithms version;
- notebook and ipykernel versions.

### Phase 3 — Beginner/intermediate regression test

Re-run known working examples:

```bat
python 01_basic_circuits\hadamard_superposition.py
python 02_bell_states\bell_state_sampler.py
python 03_primitives\statevector_sampler_current_version.py
python 03_primitives\estimator_zz_expectation.py
python 04_parameterized_circuits\real_amplitudes_ansatz.py
python 07_algorithms_intro\grover_intro.py
python 07_algorithms_intro\qft_intro.py
```

These tests confirm that new advanced additions did not disturb earlier files.

### Phase 4 — Advanced code validation

Use:

```text
docs/advanced_code_testing_protocol.md
```

and update:

```text
docs/advanced_code_status_table.md
```

### Phase 5 — Documentation validation

For each code file, check that related documentation exists:

- line-by-line explanation;
- application note;
- ontology metadata;
- expected output;
- safe modifications;
- known limitations.

### Phase 6 — Ontology validation

Check that `ontology/code_index.csv` or its addition files identify:

- file path;
- title;
- level;
- algorithm family;
- physics/mathematics concept;
- application area;
- explanation file;
- metadata file;
- test status.

### Phase 7 — GitHub issue alignment

For each advanced topic, verify that a matching GitHub issue exists:

- Advanced QC Coverage Audit
- QAOA for Optimization Teaching Unit
- Quantum Chemistry Hamiltonian Expansion
- Materials Hamiltonians and Spin Models
- Phase Estimation Teaching Unit
- Amplitude Estimation and Monte Carlo Applications
- Quantum Machine Learning Kernel Example
- Error Mitigation and Hardware Noise
- OpenQASM 3 Execution and Arithmetic Circuits
- Societal, Environmental, STEM/STEAM Application Map
- Consolidate Ontology Code Index
- Beginner-to-Advanced Learning Path

## Validation deliverables

At the end of validation, the repository should contain:

```text
docs/repository_test_report.md
docs/advanced_code_status_table.md
docs/advanced_code_testing_protocol.md
docs/beginner_to_advanced_learning_path.md
ontology/code_index.csv
```

## Definition of ready

A code family is considered contributor-ready when it has:

1. a working or clearly labeled template file;
2. expected output or expected behavior;
3. explanation file;
4. application note;
5. ontology metadata;
6. GitHub issue for improvement;
7. test status.
