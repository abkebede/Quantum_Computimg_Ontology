# Environment Setup and Jupyter Workflow

## Level

Beginner foundation.

## Purpose

This unit explains the workflow required before any quantum-computing code can be trusted. A learner must know how to create or activate the Python environment, install the required packages, verify that the correct Python executable is being used, launch Jupyter Notebook, and understand where different kinds of commands belong.

This is not a quantum algorithm yet. It is the foundation that makes every later code example reproducible.

## Key vocabulary

| Term | Meaning |
|---|---|
| `qgss_env` | The Python virtual environment used for Qiskit work. |
| Terminal / Command Prompt | The Windows command-line window where system commands are typed. |
| Python code | Code such as `import sys` or `from qiskit import QuantumCircuit`; it must run inside Python, a `.py` file, or a notebook cell. |
| `.py` file | A regular Python script. It runs from the terminal using `python filename.py`. |
| `.ipynb` file | A Jupyter notebook. It is opened in the Jupyter browser GUI and run cell by cell. |
| Kernel | The Python engine used by a Jupyter notebook. For this project, the kernel should be `Python (qgss_env)`. |
| Jupyter Notebook GUI | The browser interface launched by the command `jupyter notebook`. |

## Step 1 — Create the environment

On Windows, a fresh virtual environment can be created with:

```bat
python -m venv C:\qgss_env
```

This creates a separate Python environment located at:

```text
C:\qgss_env
```

## Step 2 — Activate the environment

```bat
C:\qgss_env\Scriptsctivate
```

After activation, the terminal prompt may show something like:

```text
(qgss_env) C:\...>
```

If Anaconda is also active, it may show:

```text
(qgss_env) (base) C:\...>
```

The important part is that `qgss_env` is active.

## Step 3 — Install Qiskit and support packages

```bat
python -m pip install --upgrade pip
pip install qiskit qiskit-aer qiskit-ibm-runtime qiskit-algorithms matplotlib pylatexenc notebook ipykernel
```

These packages support local circuits, simulators, IBM Runtime access, algorithms, notebooks, and kernel registration.

## Step 4 — Register the Jupyter kernel

```bat
python -m ipykernel install --user --name qgss_env --display-name "Python (qgss_env)"
```

This makes the environment available inside Jupyter as:

```text
Python (qgss_env)
```

## Step 5 — Verify the environment from the terminal

Use a terminal command:

```bat
python -c "import sys; print(sys.executable)"
```

Expected output:

```text
C:\qgss_env\Scripts\python.exe
```

This is different from typing Python code directly at the terminal. The following lines are Python code, not terminal commands:

```python
import sys
print(sys.executable)
```

They should be run inside a Python script or Jupyter notebook cell.

## Step 6 — Run the repository environment check

From the repository folder:

```bat
cd <YOUR_PROJECT_FOLDER>\qc-code-study-library
python 00_environment_test\environment_check.py
```

The output should report installed package versions and show a simple test circuit.

## Step 7 — Run a `.py` code file directly

Example:

```bat
python 01_basic_circuits\hadamard_superposition.py
```

This runs the entire script from beginning to end.

## Step 8 — Launch Jupyter Notebook

From the repository folder:

```bat
jupyter notebook
```

This command launches the Jupyter Notebook GUI in a browser. It does not run a Python file by itself.

Inside Jupyter:

1. Create or open a notebook.
2. Select kernel `Python (qgss_env)`.
3. Run Python code inside notebook cells.

## Step 9 — Verify the notebook kernel

Inside a notebook cell, run:

```python
import sys
print(sys.executable)
```

Expected output:

```text
C:\qgss_env\Scripts\python.exe
```

## Common beginner error

Typing this at the Windows prompt will fail:

```bat
import sys
```

because the terminal does not directly understand Python statements. The correct terminal form is:

```bat
python -c "import sys; print(sys.executable)"
```

## Safe modifications

Learners may safely modify:

- the project folder path in `cd <YOUR_PROJECT_FOLDER>\qc-code-study-library`
- the number of shots in beginner sampling examples
- the notebook Markdown explanations
- copied code inside a notebook, one line at a time

## Unsafe modifications

Learners should not casually modify:

- the real IBM API token in files that will be uploaded
- the environment path if they do not know where Python is installed
- package versions during a teaching session without recording the change
- notebook kernels without checking `sys.executable`

## Learning outcome

After this unit, a beginner should be able to say:

> I can activate the QGSS/Qiskit environment, verify the Python executable, run `.py` files, launch Jupyter Notebook, select the correct kernel, and know the difference between terminal commands and Python code.
