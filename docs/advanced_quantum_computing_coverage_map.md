# Advanced Quantum Computing Coverage Map

This document defines the advanced scope of the QC Code Study Library. The goal is not merely to collect impressive examples, but to organize advanced quantum computing by problem type, mathematical structure, algorithm family, application area, and learner pathway.

## Advanced Code Families to Cover

### 1. Algorithmic Foundations
- Quantum phase estimation
- Amplitude estimation
- Quantum Fourier transform applications
- Trotterization and Hamiltonian simulation
- Quantum walks
- Linear-combination-of-unitaries ideas
- Block-encoding concepts

### 2. Optimization
- QAOA for MaxCut
- Constraint satisfaction
- Scheduling and routing templates
- Portfolio-style toy optimization
- Resource allocation
- Penalty-function Hamiltonians

### 3. Quantum Chemistry
- Molecular Hamiltonians
- H2 ground-state VQE
- Larger molecular examples as templates
- Pauli-term Hamiltonian construction
- Ansatz choice and energy minimization
- Chemistry-to-qubit mapping notes

### 4. Materials and Condensed Matter
- Ising model
- Transverse-field Ising chain
- Heisenberg spin chain
- Hubbard model
- Tight-binding toy models
- Correlated-electron model notes
- Materials Hamiltonian documentation

### 5. Linear Algebra and Mathematical Physics
- Eigenvalue problems
- Sparse matrix observables
- Phase-estimation connection to eigenvalues
- HHL-style linear-system concept notes
- Fourier transforms and spectral analysis

### 6. Quantum Machine Learning
- Quantum feature maps
- Quantum kernels
- Variational classifiers
- Data encoding
- Kernel matrices
- Small classification templates

### 7. Sampling and Monte Carlo
- Quantum random sampling
- Amplitude/probability estimation
- Monte Carlo speedup concepts
- Risk and uncertainty estimation examples

### 8. Hardware, Noise, and Error Mitigation
- Noisy simulator comparison
- Readout-error mitigation
- Simulator vs hardware comparison
- Backend selection
- Transpilation
- Measurement counts under noise

### 9. Error Correction and Fault Tolerance
- Bit-flip code
- Phase-flip code
- Repetition code
- Syndrome measurement
- Logical qubits
- Fault-tolerance vocabulary

### 10. Cryptography and Security
- Shor's algorithm concept notes
- Period finding
- Post-quantum security motivation
- Quantum-safe transition education

### 11. OpenQASM and Low-Level Circuit Representation
- OpenQASM 3 source examples
- Reversible arithmetic
- Ripple-carry adder
- Gate decomposition
- Circuit portability

## Advanced Application Areas

- Chemistry and catalysis
- Materials discovery
- Batteries and energy storage
- Superconductors and quantum materials
- Carbon capture chemistry
- Nitrogen fixation and fertilizer chemistry
- Drug and molecular simulation
- Climate and energy-system optimization
- Logistics and resource allocation
- Cybersecurity and post-quantum transition
- Machine learning and high-dimensional data
- Particle physics and many-body quantum systems
- STEAM education and visualization

## Required Documentation for Every Advanced Code

Each advanced code should have:

1. Working code or clearly marked source-study/template code
2. Explanation file
3. Metadata YAML card
4. Application note
5. Expected output or expected behavior
6. Safe modifications
7. Limitations and hardware-readiness statement
8. Source/license information if adapted from external material

## Status Labels

Use these labels consistently:

- `tested-local`: ran successfully in the local qgss_env
- `notebook-tested`: ran successfully in Jupyter
- `source-review`: reviewed but not executed
- `template`: requires user credentials, hardware access, or additional data
- `future-work`: planned but not implemented
- `deprecated-warning`: works but uses syntax that should later be updated
