# IBM Hardware / Simulator-vs-Hardware Bell Comparison Template — Test Result

## File tested

`05_ibm_hardware/simulator_vs_hardware_bell_comparison_template.py`

## Command used

```bat
python 05_ibm_hardware\simulator_vs_hardware_bell_comparison_template.py
```

## Environment

Tested in the `qc-code-study-library` repository from the `qgss_env` Python environment.

## Output summary

The script generated a two-qubit Bell-state circuit and ran the local ideal simulator.

Observed local ideal-simulator counts:

```text
{'11': 511, '00': 489}
```

The output also stated that the hardware section is a template and should only be uncommented on a private computer. It warns not to upload API keys or token-containing notebooks to GitHub.

## Status

**PASSED — runs successfully as a simulator-plus-hardware workflow template.**

## Warning observed

```text
SyntaxWarning: invalid escape sequence '\s'
```

This warning does not stop execution. It should be corrected in a later cleanup pass by using a raw docstring or escaping the backslash.

## Classification

This file is a **hardware workflow/template**, not a live IBM hardware execution record. It safely demonstrates the Bell-state simulator comparison and preserves token-safety guidance for future hardware testing.

## Interpretation

The simulator result is consistent with the expected Bell state: measurement outcomes are concentrated in `00` and `11`, with roughly equal frequency. This is the correct ideal behavior for the Bell state produced by an H gate followed by a CNOT.

## Next improvements

- Fix the docstring escape-sequence warning.
- Add a private local-only hardware execution workflow.
- Add a template for recording backend name, job ID, shots, date, and calibration context without exposing tokens.
- Add side-by-side comparison of ideal simulator, noisy simulator, and real hardware counts.
