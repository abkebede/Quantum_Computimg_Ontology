"""
Shor/period-finding concept note as executable printout.
This is not a full Shor implementation. It documents the structure beginners must learn.
"""
steps = [
    "Choose an integer N to factor.",
    "Choose a base a with gcd(a, N) = 1.",
    "Find the period r of f(x) = a^x mod N.",
    "Use quantum phase estimation / QFT structure to estimate r.",
    "Use classical post-processing to obtain factors from r when conditions hold.",
]
print("Shor algorithm concept: factoring is reduced to period finding.")
for i, step in enumerate(steps, 1):
    print(f"{i}. {step}")
print("Repository status: concept template; full implementation is future work.")
