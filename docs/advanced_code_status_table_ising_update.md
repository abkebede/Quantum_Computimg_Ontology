# Advanced Code Status Table Update: Transverse-Field Ising Chain

Add the following row to the advanced code status table.

```markdown
| Transverse-Field Ising Chain | `12_advanced_codes/materials/transverse_field_ising_chain.py` | Working Hamiltonian-construction example | Tested — runs successfully with minor warning | Advanced | Materials physics / spin chains / many-body Hamiltonians | Fix invalid escape-sequence warning; add eigenvalues, ground-state energy, and variational expectation-value example |
```

## Suggested GitHub Issue Comment

Paste this into the relevant GitHub issue, most likely:

```text
Materials Hamiltonians and Spin Models
```

```markdown
## Test update — Transverse-Field Ising Chain

File tested:

`12_advanced_codes/materials/transverse_field_ising_chain.py`

Command used:

`python 12_advanced_codes\materials\transverse_field_ising_chain.py`

Result:

- Runs successfully: yes
- Hamiltonian type: `SparsePauliOp`
- Number of qubits: `3`
- Number of Pauli terms: `5`
- Pauli terms: `ZZI`, `IZZ`, `XII`, `IXI`, `IIX`
- Coefficients: `-1`, `-1`, `-0.5`, `-0.5`, `-0.5`

Warning:

`SyntaxWarning: invalid escape sequence '\m'`

Interpretation:

The code successfully constructs a three-qubit transverse-field Ising Hamiltonian. This validates the file as a working advanced materials-physics Hamiltonian-construction example. The next improvement should add eigenvalues, ground-state energy, and possibly a variational or time-evolution calculation.
```
