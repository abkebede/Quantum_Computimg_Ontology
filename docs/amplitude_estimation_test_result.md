# Amplitude Estimation Advanced Code Test Result

## Test summary

This file records the validation run for the amplitude/probability estimation advanced-code example.

## File tested

```text
07_algorithms_intro/amplitude_estimation_intro.py
```

## Command used

```bat
python 07_algorithms_intro\amplitude_estimation_intro.py
```

## Environment

The run was performed from the local repository:

```text
C:\Users\gutaye\Documents\QGSS_Qiskit_Qualification_Portfolio\qc-code-study-library
```

The active Python executable reported earlier in this validation session was:

```text
C:\qgss_env\Scripts\python.exe
```

Earlier environment check in the same session reported:

```text
Python version: 3.12.3
qiskit: 2.4.2
qiskit-aer: 0.17.2
qiskit-ibm-runtime: 0.47.0
qiskit-algorithms: 0.4.0
notebook: 7.6.0
ipykernel: 7.3.0
```

## Terminal output

```text
Amplitude/probability estimation intro
     ┌────────────┐┌─┐
  q: ┤ Ry(1.1593) ├┤M├
     └────────────┘└╥┘
c: 1/═══════════════╩═
                    0
Counts: {'1': 574, '0': 1426}
Estimated P(1): 0.287
True P(1): 0.3
This is sampling-based estimation, not full quantum amplitude estimation yet.
```

## Result

```text
Status: PASSED — runs successfully
Warnings: none observed
Errors: none observed
```

## Interpretation

The code prepares a one-qubit state using a rotation gate, measures the qubit many times, and estimates the probability of measuring `1` from the observed counts.

The measured estimate was:

```text
Estimated P(1): 0.287
```

The expected theoretical probability was:

```text
True P(1): 0.3
```

The result is close to the theoretical value, with the small difference expected from finite-shot sampling noise.

## Important classification

This file is currently a **sampling-based probability-estimation example**, not a full quantum amplitude estimation algorithm. It is still useful because it introduces the statistical measurement idea that amplitude estimation builds upon.

## Next improvements

- Add a short explanation of the relation between rotation angle and probability.
- Add shot-count comparison, for example 100, 1,000, and 10,000 shots.
- Add a plot showing convergence of the estimated probability.
- Later add a true amplitude-estimation circuit or Qiskit-supported amplitude-estimation workflow if compatible with the installed Qiskit version.
