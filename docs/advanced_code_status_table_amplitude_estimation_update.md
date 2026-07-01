# Advanced Code Status Table Update — Amplitude Estimation

Add the following row to `docs/advanced_code_status_table.md` or use it as a standalone validation record.

| Topic | File | Status | Tested? | Level | Application | Next improvement |
|---|---|---|---|---|---|---|
| Amplitude / probability estimation | `07_algorithms_intro/amplitude_estimation_intro.py` | Working sampling-based probability-estimation example | Tested — runs successfully | Advanced introduction | Monte Carlo, probability estimation, sampling, uncertainty | Add shot-count comparison and later add a true amplitude-estimation algorithm |

## Test result summary

```text
Counts: {'1': 574, '0': 1426}
Estimated P(1): 0.287
True P(1): 0.3
Warnings: none observed
Errors: none observed
```

## Classification note

This example should be classified carefully as:

```text
sampling-based probability estimation
```

not yet as:

```text
full quantum amplitude estimation
```

The code is still valuable because it provides the bridge between circuit measurement, probability, finite-shot uncertainty, and the later quantum amplitude-estimation algorithm.
