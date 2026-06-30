# Quantum Computing Code Study Library

**Author:** Abebe Kebede  
**Purpose:** A basic-to-advanced code-study library for learning quantum computing with Python, Qiskit, Jupyter Notebook, OpenQASM, and IBM Quantum hardware.

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
├── setup\_guides/                   Environment, Jupyter, and IBM Quantum setup
├── 00\_environment\_test/             Verify Python, Qiskit, and kernel setup
├── 01\_basic\_circuits/               One-qubit and measurement examples
├── 02\_bell\_states/                  Two-qubit entanglement examples
├── 03\_primitives/                   Sampler and Estimator examples
├── 04\_parameterized\_circuits/       Parameterized ansatz circuits
├── 05\_ibm\_hardware/                 IBM Quantum hardware templates
├── 06\_openqasm\_examples/            OpenQASM programs
├── 07\_algorithms\_intro/             Grover, QFT, and VQE introduction
├── 08\_applications\_by\_problem\_type/ Classical-to-quantum application mapping
├── ontology/                        Code ontology, metadata schema, and indexes
├── docs/                            Study method, vocabulary, test reports, and faculty notes
├── evidence/                        Screenshots and run logs
├── .github/                         Issue templates for contributors
└── .devcontainer/                   GitHub Codespaces setup
```

## Important Safety Rule

Never commit an IBM Quantum API key, token, password, or screenshot that shows a token. Use the provided templates, but replace `PASTE\_YOUR\_API\_KEY\_HERE` only on your private computer and do not upload the modified file to GitHub.

## Recommended Learning Order

1. `00\_environment\_test/environment\_check.py`
2. `01\_basic\_circuits/one\_qubit\_x\_gate.py`
3. `01\_basic\_circuits/hadamard\_superposition.py`
4. `01\_basic\_circuits/measurement\_counts.py`
5. `02\_bell\_states/bell\_state\_sampler.py`
6. `03\_primitives/estimator\_zz\_expectation.py`
7. `04\_parameterized\_circuits/real\_amplitudes\_ansatz.py`
8. `05\_ibm\_hardware/run\_bell\_on\_ibm\_hardware.py`
9. `06\_openqasm\_examples/cuccaro\_ripple\_carry\_adder.qasm`
10. `07\_algorithms\_intro/grover\_intro.py`, `qft\_intro.py`, and `vqe\_intro.ipynb`

## How to Run a Python File

```bat
C:\\qgss\_env\\Scripts\\activate
cd <YOUR\_PROJECT\_FOLDER>\\qc-code-study-library
python 01\_basic\_circuits\\hadamard\_superposition.py
```

## How to Launch Jupyter Notebook

```bat
C:\\qgss\_env\\Scripts\\activate
cd <YOUR\_PROJECT\_FOLDER>\\qc-code-study-library
jupyter notebook
```

Then select or create a notebook using the kernel:

```text
Python (qgss\_env)
```

## GitHub and Jupyter Notebook Use

This repository is GitHub-ready. It should not contain personal computer paths such as `C:\\Users\\specific-name\\...`; use `<YOUR\_PROJECT\_FOLDER>` in documentation instead.

GitHub can display `.ipynb` notebooks, but opening a notebook on GitHub usually shows a static rendering. To execute notebook cells, run the repository locally with Jupyter Notebook or use GitHub Codespaces. A `.devcontainer/devcontainer.json` file is included for Codespaces.

For details, see:

```text
docs/github\_upload\_and\_jupyter\_notebooks.md
```



## Beginner Documentation and Test Report

The Step 14 documentation records the tested workflow, vocabulary, and how the examples fit into the larger structure of quantum computing:

```
- \[Step 14 Beginner Documentation, Vocabulary, and Test Report](docs/step14\_beginner\_documentation\_vocabulary\_and\_test\_report.md)

\- \[Vocabulary and Abbreviations](docs/vocabulary\_and\_abbreviations.md)

\- \[Repository Test Report](docs/repository\_test\_report.md)

\- \[How the Examples Fit into Quantum Computing](docs/how\_examples\_fit\_in\_quantum\_computing.md)

```

These files are intended for beginners and novice users who need more than code. They explain the environment setup, terminology, tested examples, warnings, and application context.

## Quantum Computing Code Ontology

This repository now includes an `ontology/` directory. The ontology makes the library searchable by learner level, quantum concept, gate set, Qiskit object, algorithm family, mathematical structure, and application area. The goal is to support beginners, novice users, faculty, and contributors who want to understand not only how to run a code, but also what problem type the code represents.

Each code example should eventually have a metadata card describing:

* title and file path
* level: beginner, intermediate, or advanced
* code type: Python, Jupyter notebook, OpenQASM, or Markdown explanation
* source and license information
* quantum concepts and gates
* Qiskit objects and syntax
* algorithm family
* mathematical or physics structure
* application area
* expected output
* safe and unsafe modifications
* questions for line-by-line study

Contributors should read `CONTRIBUTING.md` and use the templates in `ontology/` before adding new material.

