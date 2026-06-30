# Beginner Problem-to-Algorithm Map

This map connects broad problem types to quantum-computing concepts and example codes in the repository.

| Problem type | Classical idea | Quantum concept | Example code | Level |
|---|---|---|---|---|
| Random sampling | probability distributions | measurement shots | `01_basic_circuits/measurement_counts.py` | beginner |
| Binary state preparation | bits and logic | X gate and measurement | `01_basic_circuits/one_qubit_x_gate.py` | beginner |
| Superposition | probability amplitudes | H gate | `01_basic_circuits/hadamard_superposition.py` | beginner |
| Correlation | paired outcomes | Bell state | `02_bell_states/bell_state_sampler.py` | beginner/intermediate |
| Physical measurement | average value | Estimator and observable | `03_primitives/estimator_zz_expectation.py` | intermediate |
| Tunable model | adjustable parameters | ansatz | `04_parameterized_circuits/real_amplitudes_ansatz.py` | intermediate |
| Hardware access | cloud execution | backend and API key | `05_ibm_hardware/run_bell_on_ibm_hardware.py` | intermediate |
| Reversible arithmetic | adders and logic | OpenQASM gates | `06_openqasm_examples/cuccaro_ripple_carry_adder.qasm` | advanced |
| Search | find marked item | Grover amplification | `07_algorithms_intro/grover_intro.py` | intermediate |
| Fourier analysis | transform basis | QFT | `07_algorithms_intro/qft_intro.py` | intermediate |
| Energy minimization | eigenvalue/optimization | VQE | `07_algorithms_intro/vqe_intro.ipynb` | intermediate/advanced |

## How to extend this map

For each new code added to the repository, contributors should identify:

```text
problem type
classical analog
quantum concept
algorithm family
application area
example code path
level
```
