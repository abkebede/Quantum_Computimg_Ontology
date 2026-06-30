# Application Note: Why Running on IBM Quantum Hardware Matters

## Problem Type

Hardware-aware quantum computing, noisy intermediate-scale quantum devices, experimental quantum information.

## Why This Matters

A learner can understand a circuit on paper and still not understand what happens on a real quantum processor. Running a Bell state on IBM Quantum hardware introduces the real-world layer of quantum computing:

- device noise
- gate errors
- readout errors
- decoherence
- backend selection
- transpilation
- queue time
- job IDs and reproducibility

## Societal and STEM Relevance

Real quantum hardware access supports training in:

- quantum workforce development
- experimental quantum information science
- physics and engineering education
- reproducible computational science
- cloud-based STEM laboratories
- democratized access to advanced scientific instruments

## Environmental and Materials Relevance

Hardware-aware execution is essential before quantum computing can be used seriously for advanced applications such as:

- molecular energy estimation
- materials simulation
- catalyst modeling
- battery-material research
- quantum chemistry
- condensed-matter models

A beginner Bell-state hardware run is not solving those problems yet, but it teaches the workflow needed before advanced hardware experiments are credible.

## Library Role

This module should be classified as intermediate because it requires:

- a working Qiskit environment
- IBM Quantum access
- token safety
- backend awareness
- comparison between ideal and noisy results

## Suggested Student Assignment

Run the Bell-state circuit locally and on IBM hardware. Record:

1. simulator counts
2. hardware counts
3. job ID
4. backend name
5. date of run
6. percentage of ideal outcomes
7. percentage of noisy outcomes
8. interpretation of the difference

## Key Lesson

Quantum computing is not only circuit design. It is also hardware execution, calibration, noise, and careful evidence documentation.
