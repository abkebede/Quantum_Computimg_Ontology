# Advanced Code Status Table Update — Heisenberg Spin Chain

Add the following row to `docs/advanced_code_status_table.md`.

```markdown
| Heisenberg spin-chain Hamiltonian | `12_advanced_codes/materials/heisenberg_spin_chain_hamiltonian.py` | Working example | Tested — runs successfully | Advanced | Materials physics / spin chains / quantum magnetism | Add eigenvalues, ground-state energy, ferro/antiferro comparison, and estimator-based expectation value |
```

## Validation note

This test confirms that the Heisenberg spin-chain Hamiltonian code runs and produces a valid `SparsePauliOp` representation with six Pauli terms for a three-site nearest-neighbor chain.
