# Launch Jupyter Notebook GUI

Jupyter Notebook is a browser-based graphical interface. The command below does not run a Python file. It starts a local Jupyter server and opens the notebook GUI in a web browser.

## Launch sequence

```bat
C:\qgss_env\Scripts\activate
cd <YOUR_PROJECT_FOLDER>\qc-code-study-library
jupyter notebook
```

After `jupyter notebook`, a browser window should open.

If it does not open automatically, copy the URL shown in the terminal. It will look like:

```text
http://localhost:8888/tree?token=...
```

Paste the full link into Chrome, Edge, or Firefox.

## Inside the Jupyter GUI

1. Click **New**.
2. Choose **Python (qgss_env)**.
3. Paste Python/Qiskit code into a code cell.
4. Press **Shift + Enter** to run the cell.

## Verify the kernel inside a notebook

Paste this into a Jupyter code cell:

```python
import sys
print(sys.executable)
```

Expected output:

```text
C:\qgss_env\Scripts\python.exe
```
