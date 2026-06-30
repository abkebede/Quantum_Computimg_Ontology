"""
Readout-error mitigation intro using a 1-qubit calibration matrix.

Purpose:
    Show the idea of correcting measured counts using a simple classical
    readout-confusion matrix. This is a teaching example, not a full mitigation package.
"""

import numpy as np

# Suppose true probabilities are p_true = [P(0), P(1)].
# The readout matrix maps true probabilities to observed probabilities.
# Rows are observed outcomes, columns are true outcomes.
readout_matrix = np.array([
    [0.97, 0.04],  # observed 0 if true 0 or true 1
    [0.03, 0.96],  # observed 1 if true 0 or true 1
])

observed_counts = {"0": 540, "1": 460}
shots = sum(observed_counts.values())
observed_probs = np.array([observed_counts.get("0", 0) / shots, observed_counts.get("1", 0) / shots])
mitigated_probs = np.linalg.inv(readout_matrix) @ observed_probs
mitigated_probs = np.clip(mitigated_probs, 0, 1)
mitigated_probs = mitigated_probs / mitigated_probs.sum()

print("Readout mitigation intro")
print("Observed counts:", observed_counts)
print("Observed probabilities:", observed_probs)
print("Mitigated probabilities:", mitigated_probs)
print("Teaching idea: mitigation uses calibration data to correct biased measurement outcomes.")
