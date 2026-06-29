Windows Setup: Create the QGSS/Qiskit Environment
This guide creates a local Python virtual environment named `qgss_env`.
1. Open Command Prompt
Open Windows Command Prompt or Anaconda Prompt.
2. Create the environment
```bat
python -m venv C:\qgss_env
```
3. Activate the environment
```bat
C:\qgss_env\Scripts\activate
```
The prompt should show:
```text
(qgss_env) C:\...
```
If you see `(qgss_env) (base)`, that means Anaconda's base prompt is also visible. The important check is the Python executable path.
4. Upgrade pip
```bat
python -m pip install --upgrade pip
```
5. Install Qiskit and notebook tools
```bat
pip install qiskit qiskit-aer qiskit-ibm-runtime qiskit-algorithms numpy scipy matplotlib pylatexenc notebook ipykernel
```
6. Register the Jupyter kernel
```bat
python -m ipykernel install --user --name qgss_env --display-name "Python (qgss_env)"
```
7. Verify from the terminal
```bat
python -c "import sys; print(sys.executable)"
```
Expected output:
```text
C:\qgss_env\Scripts\python.exe
```
