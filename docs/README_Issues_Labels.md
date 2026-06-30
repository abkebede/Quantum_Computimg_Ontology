# README: GitHub Issues and Labels

This document explains how GitHub Issues and labels are used in the **Quantum Computing Code Study Library** repository.

The purpose of the issue-and-label system is to organize contributions from students, faculty, collaborators, and independent learners. Issues should define clear work items. Labels should help contributors identify the level, topic, and type of work required.

---

## 1. What Issues Are For

GitHub Issues are used to track project tasks, code additions, documentation needs, testing needs, ontology updates, and application-map development.

Each issue should have:

```text
Title = short task name
Description = purpose, tasks, deliverables, suggested file locations
Comments = discussion, progress updates, questions, corrections
```

A good issue is not just a reminder. It should be a small project assignment.

---

## 2. What Labels Are For

Labels classify issues so that contributors can find work that matches their background and interest.

Labels may indicate:

- difficulty level
- type of work
- research/application area
- repository component
- testing status
- contributor suitability

Depending on GitHub permissions and workflow, an issue may have one label or several labels. If multiple labels are inconvenient, use one clear best-fit label.

---

## 3. Recommended Label Categories

### Difficulty Labels

```text
beginner
intermediate
advanced
learning-path
```

Use these to indicate the level of background expected.

### Work-Type Labels

```text
documentation
code-needed
testing-needed
qiskit-update
```

Use these to indicate the kind of work required.

### Topic and Component Labels

```text
ontology
application-map
hardware
faculty-training
```

Use these to indicate the project area or special context.

### Contributor Entry Labels

```text
good-first-issue
```

Use this for safe, well-defined tasks that a new contributor can complete without needing advanced quantum-computing knowledge.

---

## 4. Practical Single-Label System

If the repository workflow is easier with one label per issue, use the most important label only.

Suggested single-label choices:

| Issue Type | Best Single Label |
|---|---|
| Beginner testing task | `good-first-issue` |
| Advanced code module | `advanced` |
| Qiskit compatibility problem | `qiskit-update` |
| IBM Quantum hardware task | `hardware` |
| Ontology/index task | `ontology` |
| Application or societal map | `application-map` |
| Learning sequence | `learning-path` |
| General documentation | `documentation` |
| Code still needed | `code-needed` |
| Testing still needed | `testing-needed` |

---

## 5. Label Assignment for the 12 Advanced Issues

| # | Issue Title | Recommended Label(s) | Single-Label Option |
|---:|---|---|---|
| 1 | Advanced QC Coverage Audit | `advanced`, `documentation`, `ontology` | `advanced` |
| 2 | QAOA for Optimization Teaching Unit | `advanced`, `code-needed`, `application-map` | `advanced` |
| 3 | Quantum Chemistry Hamiltonian Expansion | `advanced`, `code-needed`, `application-map` | `advanced` |
| 4 | Materials Hamiltonians and Spin Models | `advanced`, `code-needed`, `application-map` | `advanced` |
| 5 | Phase Estimation Teaching Unit | `advanced`, `code-needed` | `advanced` |
| 6 | Amplitude Estimation and Monte Carlo Applications | `advanced`, `code-needed`, `application-map` | `advanced` |
| 7 | Quantum Machine Learning Kernel Example | `advanced`, `code-needed`, `application-map` | `advanced` |
| 8 | Error Mitigation and Hardware Noise | `advanced`, `hardware`, `testing-needed` | `hardware` |
| 9 | OpenQASM 3 Execution and Arithmetic Circuits | `advanced`, `code-needed`, `testing-needed`, `qiskit-update` | `qiskit-update` |
| 10 | Societal, Environmental, STEM/STEAM Application Map | `documentation`, `application-map`, `ontology` | `application-map` |
| 11 | Consolidate Ontology Code Index | `ontology`, `documentation` | `ontology` |
| 12 | Beginner-to-Advanced Learning Path | `beginner`, `intermediate`, `advanced`, `documentation` | `learning-path` |

---

## 6. Suggested Issue Description Template

Use this format when creating new issues.

```markdown
## Purpose

Explain why this issue exists and how it supports the repository.

## Tasks

- Task 1
- Task 2
- Task 3

## Deliverables

- Code file, if needed
- Explanation file, if needed
- Application note, if needed
- Ontology metadata file, if needed
- Test report, if needed

## Suggested File Locations

- `12_advanced_codes/...`
- `09_code_explanations/...`
- `10_application_notes/...`
- `ontology/examples/...`

## Notes

Add constraints, warnings, or useful references.
```

---

## 7. Suggested Good First Issue

Title:

```text
Good First Issue — Test One Beginner Code and Report the Output
```

Labels:

```text
good-first-issue
beginner
testing-needed
```

Single-label option:

```text
good-first-issue
```

Description:

```markdown
Choose one beginner code file, run it exactly as written, and report the output.

Suggested files:

- `00_environment_test/environment_check.py`
- `01_basic_circuits/one_qubit_x_gate.py`
- `01_basic_circuits/hadamard_superposition.py`
- `01_basic_circuits/measurement_counts.py`
- `02_bell_states/bell_state_sampler.py`

Deliverable:

Add a comment to this issue with:

1. file tested
2. command used
3. output
4. whether the output matched the expected result
5. any error message, if applicable
```

---

## 8. Recommended Label Descriptions

| Label | Description |
|---|---|
| `beginner` | Entry-level task suitable for new learners. |
| `intermediate` | Requires some Qiskit and quantum-circuit background. |
| `advanced` | Requires advanced quantum-computing, physics, or algorithm knowledge. |
| `learning-path` | Related to sequencing material from beginner to advanced. |
| `documentation` | Requires writing, editing, explanation, or organization. |
| `code-needed` | Requires a new or improved code example. |
| `testing-needed` | Requires running code and reporting output/errors. |
| `qiskit-update` | Requires checking compatibility with current Qiskit syntax. |
| `ontology` | Related to metadata, classification, indexing, or knowledge organization. |
| `application-map` | Related to societal, environmental, scientific, or STEM/STEAM applications. |
| `hardware` | Related to IBM Quantum hardware, noisy devices, backend execution, or hardware results. |
| `faculty-training` | Useful for faculty, workshop, curriculum, or training use. |
| `good-first-issue` | Safe starting task for a new contributor. |

---

## 9. Working Principle

The issue system should help the repository grow in a disciplined way:

```text
Code → explanation → application → ontology → testing → learning path
```

Every important code example should eventually have:

- a working source file
- a line-by-line explanation
- an application note
- an ontology metadata card
- a tested-output record

