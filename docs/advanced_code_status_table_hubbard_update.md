# Advanced Code Status Table Update: Hubbard Model

Add the following row to `docs/advanced_code_status_table.md` or use it as a separate validation record.

| Topic | File | Status | Tested? | Level | Application | Next improvement |
|---|---|---|---|---|---|---|
| Hubbard model — two-site simplified | `12_advanced_codes/materials/hubbard_model_two_site_simplified.py` | Working Hamiltonian-construction example | Tested — runs successfully | Advanced | Correlated electrons / materials physics / Hubbard-like models | Clarify simplified status; add fermion-to-qubit mapping version; add eigenvalue or expectation-value calculation |

## Test Evidence

```text
Simplified Hubbard-like two-qubit Hamiltonian:
SparsePauliOp(['XX', 'YY', 'ZZ', 'ZI', 'IZ'],
              coeffs=[-1.  +0.j, -1.  +0.j,  0.5 +0.j,  0.25+0.j,  0.25+0.j])
Teaching use: connects correlated-electron models to Pauli Hamiltonians.
```
