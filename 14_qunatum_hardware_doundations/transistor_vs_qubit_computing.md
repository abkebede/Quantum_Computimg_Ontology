# Transistor Computing vs Qubit Computing

## Classical transistor computing

In a classical computer, the transistor is engineered to behave as a reliable switch. A voltage level represents a bit value.

```text
low voltage  -> 0
high voltage -> 1
```

Many transistors are combined into logic gates such as NOT, AND, OR, NAND, and NOR. These gates are assembled into processors, memory, and digital systems.

## Quantum computing

In a quantum computer, the physical element is engineered to behave as a controllable two-level quantum system. These two selected states form the computational basis:

```text
|0> and |1>
```

Unlike a classical bit, a qubit can be prepared in a superposition:

```text
a|0> + b|1>
```

Quantum gates are controlled physical operations that rotate, phase-shift, entangle, or measure these quantum states.

## Key comparison

| Classical computing | Quantum computing |
|---|---|
| Transistor | Qubit device |
| Bit | Qubit |
| Voltage level | Quantum state amplitude and phase |
| Logic gate | Quantum gate |
| CMOS circuit | Quantum processor |
| Mostly deterministic logic | Probabilistic measurement outcomes |
| Error suppression by device engineering | Error suppression plus quantum error correction |
| Room-temperature chips | Often cryogenic, vacuum, optical, or low-noise hardware |

## Student message

A quantum gate is not merely a symbol. It corresponds to a controlled physical process applied to a quantum device.
