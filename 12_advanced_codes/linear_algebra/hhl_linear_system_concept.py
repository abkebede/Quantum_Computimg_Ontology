"""
HHL-style linear-system concept note.
This is not a full HHL implementation. It maps the problem Ax=b to quantum algorithm ideas.
"""
print("Linear-system problem: solve A x = b")
print("Quantum algorithm family: HHL and descendants")
print("Core ideas:")
print("1. Encode vector b into a quantum state |b>.")
print("2. Use phase estimation to access eigenvalues of A.")
print("3. Apply controlled rotations related to 1/lambda.")
print("4. Uncompute phase estimation.")
print("5. Measure observables of |x>, not necessarily all entries of x.")
print("Teaching status: concept template for advanced mathematical physics and linear algebra.")
