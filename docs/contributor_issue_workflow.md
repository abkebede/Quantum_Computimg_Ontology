# Contributor Issue Workflow

This guide explains how students, faculty, and colleagues should use GitHub Issues in the `qc-code-study-library` project.

## 1. Choose an issue

Start from the GitHub Issues tab. Choose an issue based on your experience level and interest.

Recommended entry points:

| Contributor level | Suggested issue type |
|---|---|
| Beginner | test one code file and report output |
| Intermediate | improve explanations, expected outputs, and safe modifications |
| Advanced | expand algorithms, Hamiltonians, error mitigation, QAOA, QML, or hardware comparison |
| Faculty/mentor | review accuracy, applications, ontology, and learning path |

## 2. Read the issue body first

The issue body should contain:

- purpose;
- tasks;
- deliverables;
- suggested files;
- notes.

Comments should be used for progress reports, questions, and updates.

## 3. Use labels to find work

Example labels:

```text
beginner
intermediate
advanced
documentation
ontology
application-map
code-needed
testing-needed
hardware
qiskit-update
learning-path
good-first-issue
faculty-training
```

A single issue may have more than one label, but a single combined label is also acceptable when the meaning is clearer.

Example:

```text
Beginner-to-Advanced Learning Path → learning-path
```

## 4. Report work in a comment

When testing code, add a comment like this:

```markdown
## Test report

- File tested:
- Command used:
- Python version:
- Qiskit version:
- Output:
- Result: PASSED / PASSED WITH WARNING / FAILED / PARTIAL
- Notes:
```

When improving documentation, add a comment like this:

```markdown
## Documentation update

- File improved:
- What was changed:
- What still needs work:
```

## 5. Do not commit secrets

Never upload:

- IBM Quantum API tokens;
- local absolute paths such as `C:\Users\...`;
- passwords;
- private keys;
- personal data.

Use placeholders such as:

```text
PASTE_YOUR_API_KEY_HERE
```

or environment variables.

## 6. Suggested branch names

When working locally, use clear branch names:

```text
test-qaoa-maxcut
update-vqe-explanation
add-ising-application-note
fix-qiskit-api-warning
advanced-code-audit
```

## 7. Suggested commit messages

Examples:

```text
Test QAOA MaxCut example
Add explanation for phase estimation
Update advanced code status table
Add ontology metadata for quantum kernel example
Fix deprecated Qiskit syntax in parameterized circuit
```

## 8. Close an issue only when deliverables are complete

Before closing an issue, check:

- code file exists;
- code was tested or labeled as template;
- documentation exists;
- application note exists;
- ontology metadata exists;
- status table was updated;
- any warnings or limitations were recorded.

## 9. Good first issue template

Title:

```text
Good First Issue — Test One Code and Report the Output
```

Description:

```markdown
Choose one code file, run it exactly as written, and report the output.

Suggested files:

- 00_environment_test/environment_check.py
- 01_basic_circuits/hadamard_superposition.py
- 02_bell_states/bell_state_sampler.py
- 03_primitives/statevector_sampler_current_version.py
- 07_algorithms_intro/grover_intro.py

Deliverable:

Add a comment with:

1. file tested;
2. command used;
3. output;
4. whether the output matched the expected result;
5. any warnings or errors.
```

Suggested labels:

```text
good-first-issue
testing-needed
beginner
```
