# Teaching Unit: Running a Bell State on IBM Quantum Hardware

## Level

Intermediate.

This unit assumes the learner already understands one-qubit gates, measurement, Bell states, simulator counts, and the difference between a terminal command and a Jupyter notebook cell.

## Code File

```text
05_ibm_hardware/run_bell_on_ibm_hardware.py
```

## Purpose

This example moves from local simulation to cloud-accessed real quantum hardware. The learner prepares a Bell-state circuit, connects to IBM Quantum using a saved account credential, selects a backend, transpiles the circuit for the device, submits a Sampler job, retrieves counts, and interprets noisy real-hardware results.

## Safety Rule

Never commit a real IBM Quantum API key to GitHub. Never paste a real token into a public notebook, screenshot, README, issue, or code file.

Use templates such as:

```python
TOKEN = "PASTE_YOUR_API_KEY_HERE"
```

only on a private computer. Do not upload the modified token file.

## Main Ideas

### 1. IBM Quantum account

An IBM Quantum account gives the user access to cloud quantum backends. In Qiskit, the account is usually accessed through `QiskitRuntimeService`.

### 2. API key or token

The API key is a private credential. It is not a password to show in teaching materials. It allows Qiskit to authenticate with IBM Quantum services.

### 3. Backend

A backend is the target system where the circuit is run. It may be a simulator or a real quantum processor.

### 4. Transpilation

Real devices do not support arbitrary circuits directly. Transpilation rewrites the circuit into the gates and connectivity supported by the selected backend.

### 5. SamplerV2

The Sampler primitive returns measurement results from repeated circuit execution. For a Bell state, the ideal outcomes are `00` and `11`.

## Expected Ideal Result

For the Bell state

```text
(|00> + |11>)/sqrt(2)
```

the ideal result is approximately half `00` and half `11`.

On a noiseless simulator:

```text
{'00': about 500, '11': about 500}
```

On real hardware, extra outcomes may appear:

```text
{'00': many, '11': many, '01': small, '10': small}
```

The `01` and `10` outcomes indicate noise, readout error, gate error, decoherence, calibration limitations, or other device imperfections.

## Line-by-Line Study Questions

1. Which line creates the Bell-state circuit?
2. Which line loads the IBM Quantum account?
3. Which line selects a backend?
4. Which line transpiles the circuit?
5. Which line submits the job?
6. Which line retrieves the counts?
7. Which outcomes are ideal for a Bell state?
8. Which outcomes indicate noise?

## Safe Modifications

- Change the number of shots.
- Run the same Bell circuit on a simulator and compare results.
- Select a different least-busy backend if available.
- Save the job ID in a private run log.
- Compare hardware counts to ideal simulator counts.

## Unsafe or Risky Modifications

- Do not paste a real token into a file that will be committed to GitHub.
- Do not change backend-specific code without understanding transpilation.
- Do not assume real hardware will match ideal simulation exactly.
- Do not interpret all unexpected results as code failure; real devices are noisy.

## Application Connection

This example is the first bridge from textbook quantum circuits to real quantum technology. It helps learners understand that real quantum computing includes hardware constraints, noise, queue time, calibration, and reproducibility issues.

## Beginner Summary

The Bell circuit tells us what should happen ideally. The IBM hardware run teaches us what happens on an actual quantum device. The difference between the two is not a failure; it is the beginning of hardware-aware quantum computing.
