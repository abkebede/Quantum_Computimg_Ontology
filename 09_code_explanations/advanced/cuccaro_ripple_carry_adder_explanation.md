# Teaching Unit: OpenQASM Cuccaro Ripple-Carry Adder

## File studied

```text
06_openqasm_examples/cuccaro_ripple_carry_adder.qasm
```

## Level

Advanced beginner to advanced, depending on learner background.

This file is more advanced than the one-qubit, Bell-state, Sampler, Estimator, Grover, and QFT examples because it introduces a lower-level quantum programming language and reversible arithmetic.

## What the code does

This OpenQASM 3 program implements a four-bit quantum ripple-carry adder based on the Cuccaro adder. It adds two binary numbers:

```text
a = 0001₂ = 1₁₀
b = 1111₂ = 15₁₀
```

The expected sum is:

```text
0001₂ + 1111₂ = 10000₂ = 16₁₀
```

Because the `b` register has only four qubits, the low four bits of the result are stored in `b`, and the overflow bit is stored in `cout`.

Expected final structure:

```text
b    = 0000
cout = 1
ans  = 10000
```

## Why this code matters

Most beginner quantum circuits show gates, measurement, and entanglement. This example shows something different: **quantum arithmetic**.

Quantum arithmetic is important because advanced algorithms often need reversible subroutines for:

```text
integer addition
modular arithmetic
oracles
phase estimation
period finding
cryptography-related algorithms
Hamiltonian simulation support circuits
fault-tolerant algorithm design
```

## Main concepts

```text
OpenQASM 3
custom gates
controlled-NOT gate
Toffoli gate
reversible computation
binary addition
carry propagation
majority gate
unmajority cleanup
measurement into classical bits
```

## OpenQASM syntax review

### Version declaration

```qasm
OPENQASM 3;
```

This states that the file uses OpenQASM version 3.

### Standard gate library

```qasm
include "stdgates.inc";
```

This imports standard gates such as:

```text
x
cx
ccx
```

where:

```text
x   = NOT gate
cx  = controlled-NOT gate
ccx = Toffoli gate
```

### Custom gate definition

```qasm
gate majority a, b, c {
    cx c, b;
    cx c, a;
    ccx a, b, c;
}
```

This defines a reusable three-qubit gate called `majority`.

The purpose of `majority` is to propagate carry information forward during addition.

### Uncomputation gate

```qasm
gate unmaj a, b, c {
    ccx a, b, c;
    cx c, a;
    cx a, b;
}
```

The `unmaj` gate runs a cleanup operation. It helps produce the sum bits while reversing temporary carry information. This is an important quantum-computing idea because quantum circuits must be reversible.

## Registers

```qasm
qubit[1] cin;
qubit[4] a;
qubit[4] b;
qubit[1] cout;
bit[5] ans;
```

Meaning:

```text
cin   = input carry bit
a     = first 4-bit input number
b     = second 4-bit input number and result register
cout  = final carry-out bit
ans   = 5-bit classical measured answer
```

## Input values

```qasm
uint[4] a_in = 1;
uint[4] b_in = 15;
```

These classical unsigned integers are used to prepare the quantum registers.

The binary values are:

```text
a_in = 0001
b_in = 1111
```

## Initialization

```qasm
reset cin;
reset a;
reset b;
reset cout;
```

This prepares all qubits in the state `|0>`.

## Loading the input numbers

```qasm
for i in [0: 3] {
  if (bool(a_in[i])) x a[i];
  if (bool(b_in[i])) x b[i];
}
```

This loop examines each bit of the classical input values. If the bit is 1, the code applies an `x` gate to the corresponding qubit.

The `x` gate changes:

```text
|0> → |1>
```

So this block loads binary input values into quantum computational-basis states.

## Carry propagation

```qasm
majority cin[0], b[0], a[0];
for i in [0: 2] {
  majority a[i], b[i + 1], a[i + 1];
}
```

This pushes the carry information forward from the least significant bit toward the most significant bit.

This is why the circuit is called a ripple-carry adder: the carry ripples through the bit positions.

## Carry-out

```qasm
cx a[3], cout[0];
```

This stores the final carry into `cout`.

For this example, the final carry should be 1 because:

```text
15 + 1 = 16
```

and 16 requires five bits.

## Uncomputation

```qasm
for i in [2: -1: 0] {
  unmaj a[i], b[i + 1], a[i + 1];
}
unmaj cin[0], b[0], a[0];
```

This runs backward through the adder and cleans up the temporary carry information.

This step is crucial in quantum computing. Temporary information cannot simply be erased arbitrarily. It must be uncomputed reversibly.

## Measurement

```qasm
measure b[0:3] -> ans[0:3];
measure cout[0] -> ans[4];
```

This measures the low four bits of the result from `b` and the overflow bit from `cout`.

For the given input, the expected answer is:

```text
ans = 10000
```

## Safe modifications

Beginners should first modify only the input values:

```qasm
uint[4] a_in = 3;
uint[4] b_in = 5;
```

Then predict:

```text
3 + 5 = 8 = 01000₂
```

Other safe input trials:

| a_in | b_in | Decimal sum | Expected 5-bit result |
|---:|---:|---:|---|
| 1 | 15 | 16 | 10000 |
| 3 | 5 | 8 | 01000 |
| 7 | 8 | 15 | 01111 |
| 15 | 15 | 30 | 11110 |
| 6 | 9 | 15 | 01111 |

## Unsafe modifications for beginners

Do not modify these sections until you understand reversible arithmetic:

```qasm
gate majority a, b, c { ... }
gate unmaj a, b, c { ... }
```

Do not casually modify:

```qasm
majority cin[0], b[0], a[0];
for i in [0: 2] { ... }
cx a[3], cout[0];
for i in [2: -1: 0] { ... }
unmaj cin[0], b[0], a[0];
```

Changing these lines may still produce a circuit, but it may no longer perform addition.

## Current repository status

This file has been source-reviewed. It has not yet been executed through a Python OpenQASM 3 runner inside the repository.

A future repository task should add:

```text
06_openqasm_examples/run_qasm_file.py
```

That runner should test which OpenQASM 3 features are supported in the local Qiskit environment.

## Beginner questions

1. What is the difference between a quantum register and a classical bit register?
2. Why does adding two four-bit numbers require a five-bit answer register?
3. What is the role of the Toffoli gate in the adder?
4. Why is uncomputation necessary?
5. Which lines define the arithmetic logic, and which lines only define the input values?
6. What happens if `a_in` and `b_in` are changed?
7. Why is this example more advanced than the Bell-state circuit?

## How this fits in the larger library

```text
Basic gates and measurement
→ Bell states and two-qubit logic
→ Primitives and observables
→ Parameterized circuits
→ Algorithms such as Grover and QFT
→ Reversible arithmetic and OpenQASM
→ Advanced algorithm subroutines
```

This example is a bridge from circuit learning to arithmetic circuits used in advanced quantum algorithm design.
