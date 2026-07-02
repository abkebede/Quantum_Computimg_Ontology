# Hardware-to-Gate Mapping Table

| Hardware concept | Gate-level concept | Example |
|---|---|---|
| Calibrated microwave pulse | Single-qubit rotation | RX(theta), RY(theta) |
| Virtual frame update | Phase gate | RZ(phi) |
| Controlled interaction | Entangling gate | CZ, CNOT, iSWAP |
| Resonator response | Measurement | measure q -> c |
| Repeated execution | Shots | histogram of outcomes |
| Classical feedback | Adaptive circuit | reset, parameter update |
| Noise and decoherence | Gate/readout error | error mitigation or correction |

## Interpretation

A gate is a compact software-level representation of an underlying calibrated physical process.
