# Primitives Teaching Unit Update

This is **not a full replacement** of the repository. It is a partial update for the existing project folder:

```text
qc-code-study-library
```

## Added files

```text
09_code_explanations/intermediate/sampler_and_statevector_sampler_explanation.md
10_application_notes/intermediate/sampler_and_estimator_primitives_application_note.md
ontology/examples/sampler_and_statevector_sampler_metadata.yaml
ontology/code_index_primitives_addition.csv
```

## Purpose

This update adds a teaching unit on Qiskit primitives, with emphasis on the difference between running circuits for measurement outcomes and evaluating quantum states for meaningful quantities.

The key beginner-to-intermediate idea is:

```text
Circuit -> Sampler -> measurement counts/probabilities
Circuit + Observable -> Estimator -> expectation value
```

This unit supports students who already know one-qubit gates, measurement, and Bell states, and are ready to understand how quantum circuits become computational tools.

## Suggested commit message

```text
Add Qiskit primitives teaching unit and metadata
```
