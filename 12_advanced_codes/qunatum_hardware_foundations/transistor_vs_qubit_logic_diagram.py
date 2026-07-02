"""Simple visual comparison of transistor computing and qubit computing."""
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.axis('off')

left = ["Voltage", "Transistor", "Logic gate", "Classical circuit", "Bit result"]
right = ["Control pulse", "Qubit device", "Quantum gate", "Quantum circuit", "Measurement result"]

for i, txt in enumerate(left):
    ax.text(0.1 + i*0.17, 0.7, txt, ha='center', va='center', bbox=dict(boxstyle='round', fc='white'))
    if i < len(left)-1:
        ax.annotate('', xy=(0.16+i*0.17,0.7), xytext=(0.04+i*0.17,0.7), arrowprops=dict(arrowstyle='->'))

for i, txt in enumerate(right):
    ax.text(0.1 + i*0.17, 0.3, txt, ha='center', va='center', bbox=dict(boxstyle='round', fc='white'))
    if i < len(right)-1:
        ax.annotate('', xy=(0.16+i*0.17,0.3), xytext=(0.04+i*0.17,0.3), arrowprops=dict(arrowstyle='->'))

ax.text(0.02, 0.7, 'Classical', ha='left', va='center', fontweight='bold')
ax.text(0.02, 0.3, 'Quantum', ha='left', va='center', fontweight='bold')
ax.set_title('Transistor Computing vs Qubit Computing')
plt.tight_layout()
plt.show()
