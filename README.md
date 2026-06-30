# Quantum Computing Code Study Library

**Author:** Abebe Kebede  
**Purpose:** A basic-to-advanced code-study library for learning quantum computing with Python, Qiskit, Jupyter Notebook, OpenQASM, and IBM Quantum hardware.

**Call for Contribution and Participation:** [Start here for contributors](docs/contributor_start_here.md)

This repository is designed for faculty and student training. The method is simple:

1. Run working code exactly as written.
2. Study the code line by line.
3. Identify the Python syntax, Qiskit syntax, and quantum meaning.
4. Modify one line at a time.
5. Predict the result before running.
6. Compare prediction with the actual output.
7. Record evidence, screenshots, outputs, and interpretation.

## Repository Structure

```text
qc-code-study-library/
├── setup_guides/                   Environment, Jupyter, and IBM Quantum setup
├── 00_environment_test/             Verify Python, Qiskit, and kernel setup
├── 01_basic_circuits/               One-qubit and measurement examples
├── 02_bell_states/                  Two-qubit entanglement examples
├── 03_primitives/                   Sampler and Estimator examples
├── 04_parameterized_circuits/       Parameterized ansatz circuits
├── 05_ibm_hardware/                 IBM Quantum hardware templates
├── 06_openqasm_examples/            OpenQASM programs
├── 07_algorithms_intro/             Grover, QFT, and VQE introduction
├── 08_applications_by_problem_type/ Classical-to-quantum application mapping
├── 09_code_explanations/            Line-by-line teaching units
├── 10_application_notes/            Application notes by level and problem type
├── ontology/                        Code ontology, metadata schema, and indexes
├── docs/                            Study method, vocabulary, test reports, and faculty notes
├── evidence/                        Screenshots and run logs
├── .github/                         Issue templates for contributors
└── .devcontainer/                   GitHub Codespaces setup
```

## Important Safety Rule

Never commit an IBM Quantum API key, token, password, or screenshot that shows a token. Use the provided templates, but replace `PASTE_YOUR_API_KEY_HERE` only on your private computer and do not upload the modified file to GitHub.

## Recommended Learning Order

Beginners should read the Step 14 documentation before running the advanced examples.

1. `00_environment_test/environment_check.py`
2. `01_basic_circuits/one_qubit_x_gate.py`
3. `01_basic_circuits/hadamard_superposition.py`
4. `01_basic_circuits/measurement_counts.py`
5. `02_bell_states/bell_state_sampler.py`
6. `03_primitives/estimator_zz_expectation.py`
7. `04_parameterized_circuits/real_amplitudes_ansatz.py`
8. `05_ibm_hardware/run_bell_on_ibm_hardware.py`
9. `06_openqasm_examples/cuccaro_ripple_carry_adder.qasm`
10. `07_algorithms_intro/grover_intro.py`, `qft_intro.py`, and `vqe_intro.ipynb`

## Complete Teaching Units

The repository now includes complete teaching units that connect code, line-by-line explanation, application context, and ontology metadata.

### Beginner Unit 1 — Hadamard Superposition

- [Hadamard Superposition — Complete Beginner Teaching Unit](09_code_explanations/beginner/hadamard_superposition_explanation.md)
- [Hadamard Superposition Application Note](10_application_notes/beginner/hadamard_superposition_application_note.md)
- [Hadamard Superposition Metadata Card](ontology/examples/hadamard_superposition_metadata.yaml)

### Beginner-to-Intermediate Unit 2 — Bell State and ZZ Estimator

- [Bell State and ZZ Estimator — Complete Teaching Unit](09_code_explanations/beginner/bell_state_and_zz_estimator_explanation.md)
- [Bell State and ZZ Estimator Application Note](10_application_notes/intermediate/bell_state_and_zz_estimator_application_note.md)
- [Bell State and ZZ Estimator Metadata Card](ontology/examples/bell_state_and_zz_estimator_metadata.yaml)

These modules show the standard format for future code entries: code, line-by-line explanation, syntax, quantum meaning, safe modifications, application note, and ontology metadata.

## How to Run a Python File

```bat
C:\qgss_env\Scripts\activate
cd <YOUR_PROJECT_FOLDER>\qc-code-study-library
python 01_basic_circuits\hadamard_superposition.py
```

## How to Launch Jupyter Notebook

```bat
C:\qgss_env\Scripts\activate
cd <YOUR_PROJECT_FOLDER>\qc-code-study-library
jupyter notebook
```

Then select or create a notebook using the kernel:

```text
Python (qgss_env)
```

## GitHub and Jupyter Notebook Use

This repository is GitHub-ready. It should not contain personal computer paths such as `C:\Users\specific-name\...`; use `<YOUR_PROJECT_FOLDER>` in documentation instead.

GitHub can display `.ipynb` notebooks, but opening a notebook on GitHub usually shows a static rendering. To execute notebook cells, run the repository locally with Jupyter Notebook or use GitHub Codespaces. A `.devcontainer/devcontainer.json` file is included for Codespaces.

For details, see:

[GitHub Upload and Jupyter Notebooks](docs/github_upload_and_jupyter_notebooks.md)

## Beginner Documentation and Test Report

The Step 14 documentation records the tested workflow, vocabulary, and how the examples fit into the larger structure of quantum computing:

- [Step 14 Beginner Documentation, Vocabulary, and Test Report](docs/step14_beginner_documentation_vocabulary_and_test_report.md)
- [Vocabulary and Abbreviations](docs/vocabulary_and_abbreviations.md)
- [Repository Test Report](docs/repository_test_report.md)
- [How the Examples Fit into Quantum Computing](docs/how_examples_fit_in_quantum_computing.md)

These files are intended for beginners and novice users who need more than code. They explain the environment setup, terminology, tested examples, warnings, and application context.

## Quantum Computing Code Ontology

This repository includes an `ontology/` directory that serves as the public contribution and classification layer of the project. The ontology makes the library searchable by learner level, quantum concept, gate set, Qiskit object, algorithm family, mathematical structure, and application area. The goal is to support beginners, novice users, faculty, and contributors who want to understand not only how to run a code, but also what problem type the code represents.

Each code example should eventually have a metadata card describing:

- title and file path
- level: beginner, intermediate, or advanced
- code type: Python, Jupyter notebook, OpenQASM, or Markdown explanation
- source and license information
- quantum concepts and gates
- Qiskit objects and syntax
- algorithm family
- mathematical or physics structure
- application area
- expected output
- safe and unsafe modifications
- questions for line-by-line study

Contributors should read `CONTRIBUTING.md` and use the templates in `ontology/` before adding new material.
