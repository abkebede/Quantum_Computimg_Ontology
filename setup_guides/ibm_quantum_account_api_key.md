# IBM Quantum Account and API Key Guide

This guide explains how to prepare IBM Quantum hardware access.

## 1. Create or open an IBM Quantum account

Go to the IBM Quantum Platform and sign in or create an account.

## 2. Find or create the API key

From the IBM Quantum dashboard, find or create your API key. Copy it to a secure private location such as a password manager.

## 3. Never expose the API key

Do not put the API key in:

- GitHub repositories
- screenshots
- notebooks that will be shared
- reports
- README files
- ChatGPT messages
- email attachments

## 4. Save account locally

Use this template only on your private computer. Replace the placeholder with your real API key, run it once, then delete or hide the real token.

```python
from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    channel="ibm_quantum_platform",
    token="PASTE_YOUR_API_KEY_HERE",
    overwrite=True
)
```

## 5. Test saved account

```python
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
print("Selected backend:", backend.name)
```

If this works, Qiskit can access IBM Quantum hardware through your saved credentials.
