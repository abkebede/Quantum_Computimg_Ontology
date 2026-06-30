# Advanced Code Testing Protocol

This protocol explains how to test the advanced files in `qc-code-study-library` without confusing working examples, hardware templates, and concept templates.

## 1. Start from the correct environment

Activate the same environment used for the earlier repository tests.

Example Windows command:

```bat
C:\qgss_env\Scripts\activate
```

Then confirm Python and Qiskit:

```bat
python 00_environment_test\environment_check.py
```

Record the output in the test report.

## 2. Test one file at a time

Run one code file, inspect the output, and record the result before moving to the next file.

Example:

```bat
python 07_algorithms_intro\qaoa_maxcut_intro.py
```

Do not run many files at once until the status of each file is known.

## 3. Classify the file correctly

Each tested file should be classified as one of the following:

| Classification | Meaning |
|---|---|
| Working example | Runs directly and produces the expected output. |
| Working with warning | Runs but produces deprecation warnings or nonfatal warnings. |
| Concept template | Useful for teaching, but not expected to run as a finished program. |
| Requires hardware/account | Needs IBM Quantum access or account setup. |
| Needs API update | Fails because library syntax has changed or dependencies are missing. |
| Needs documentation | Runs, but output is unclear for students. |

## 4. Record exact output

For each code file, record:

- command used;
- printed output;
- plots generated;
- warnings;
- traceback errors;
- whether the output matches the expected physics or algorithm.

Use this template:

```markdown
## Test: <file path>

- Command:
- Output:
- Expected result:
- Actual result:
- Passed? Yes / No / Partial
- Warning messages:
- Error messages:
- Interpretation:
```

## 5. Handle warnings carefully

Warnings are not always failures. Examples:

- A deprecation warning means the code may run now but should be updated.
- A missing optional package may mean the file needs dependency documentation.
- A hardware-backend warning may be normal if the user is not connected to IBM Quantum.

Mark these as **working with warning** or **needs API review**, not automatically failed.

## 6. Hardware-code rule

Files under `05_ibm_hardware/` should never include a real API token.

A safe hardware file should:

- use placeholders or environment variables;
- explain token setup outside the code;
- avoid printing private credentials;
- clearly separate simulator testing from backend execution.

## 7. OpenQASM rule

OpenQASM files may be valid source examples even if the repository does not yet include a runner.

For OpenQASM 3 arithmetic circuits, test status may be:

```text
Source reviewed; execution runner needed.
```

## 8. Priority testing order

Recommended order:

1. `07_algorithms_intro/qaoa_maxcut_intro.py`
2. `07_algorithms_intro/phase_estimation_intro.py`
3. `12_advanced_codes/chemistry/h2_hamiltonian_vqe_grid_search.py`
4. `12_advanced_codes/materials/transverse_field_ising_chain.py`
5. `12_advanced_codes/materials/heisenberg_spin_chain_hamiltonian.py`
6. `12_advanced_codes/qml/quantum_kernel_intro.py`
7. `12_advanced_codes/error_mitigation/readout_mitigation_intro.py`
8. `12_advanced_codes/error_correction/bit_flip_repetition_code.py`
9. `12_advanced_codes/quantum_simulation/trotterized_ising_time_evolution.py`
10. `05_ibm_hardware/simulator_vs_hardware_bell_comparison_template.py`
11. `06_openqasm_examples/openqasm3_runner_notes.py`
12. `06_openqasm_examples/cuccaro_ripple_carry_adder.qasm`

## 9. Pass/fail notation

Use these labels in reports:

```text
PASSED
PASSED WITH WARNING
PARTIAL / TEMPLATE
SOURCE REVIEW ONLY
FAILED — NEEDS FIX
FAILED — MISSING DEPENDENCY
FAILED — QISKIT API UPDATE NEEDED
```
