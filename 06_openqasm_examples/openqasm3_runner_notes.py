"""
OpenQASM 3 runner notes.

Purpose:
    Explain why the Cuccaro adder .qasm file is currently treated as a source-study
    example rather than guaranteed executable code in every Qiskit environment.
"""

from pathlib import Path

qasm_file = Path(__file__).with_name("cuccaro_ripple_carry_adder.qasm")
print("OpenQASM source file:", qasm_file)
print("Exists:", qasm_file.exists())
if qasm_file.exists():
    text = qasm_file.read_text(encoding="utf-8")
    print("First 500 characters:")
    print(text[:500])

print("\nNote:")
print("OpenQASM 3 support can depend on the installed parser and Qiskit version.")
print("This adder uses OpenQASM 3 features such as uint, for loops, if statements, and custom gates.")
print("Therefore it is currently classified as an advanced source-study example.")
