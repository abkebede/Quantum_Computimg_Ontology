# GitHub Issue Roadmap

Use GitHub Issues to organize the next phase of work. Each issue should be small enough for a student or colleague to complete.

## Immediate Issues

### 1. Test Beginner Codes
**Goal:** Confirm that all beginner codes run in `qgss_env`.

Checklist:
- `00_environment_test/environment_check.py`
- `01_basic_circuits/one_qubit_x_gate.py`
- `01_basic_circuits/hadamard_superposition.py`
- `01_basic_circuits/measurement_counts.py`

### 2. Fix Known Warnings
**Goal:** Clean warnings that confuse beginners.

Checklist:
- Fix invalid escape sequence warning in `environment_check.py`.
- Add note about `RealAmplitudes` deprecation.
- Consider updating to the newer `real_amplitudes` function in a future-compatible example.

### 3. Consolidate Ontology Index
**Goal:** Keep one master `ontology/code_index.csv`.

Checklist:
- Merge individual `code_index_*_addition.csv` files into `ontology/code_index.csv`.
- Check that every teaching unit has one metadata card.
- Check that every metadata card points to the correct code and explanation files.

### 4. Add QAOA Teaching Unit
**Goal:** Add a first optimization example.

Checklist:
- Small MaxCut or two-node/three-node optimization problem.
- Qiskit code.
- Line-by-line explanation.
- Metadata card.
- Application note on optimization.

### 5. Add Materials / Chemistry Application Module
**Goal:** Connect VQE to real STEM problems.

Checklist:
- Explain Hamiltonians in chemistry and materials.
- Add small educational model: H2, Heisenberg model, or Ising model.
- Explain limitations of near-term quantum hardware.

## Contributor Labels to Use

Suggested labels:

```text
beginner
intermediate
advanced
documentation
code-test
ontology
application-note
bug
qiskit-version
hardware
good-first-issue
```
