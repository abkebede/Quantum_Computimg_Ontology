"""Classical-quantum hybrid workflow diagram."""
import matplotlib.pyplot as plt

steps = [
    'Algorithm',
    'Circuit',
    'Transpile',
    'Pulse/control',
    'Quantum chip',
    'Readout',
    'Classical processing',
    'Feedback'
]

fig, ax = plt.subplots(figsize=(11, 3.8))
ax.axis('off')
for i, s in enumerate(steps):
    x = 0.06 + i*0.12
    ax.text(x, 0.55, s, ha='center', va='center', bbox=dict(boxstyle='round', fc='white'))
    if i < len(steps)-1:
        ax.annotate('', xy=(x+0.06,0.55), xytext=(x+0.025,0.55), arrowprops=dict(arrowstyle='->'))
# feedback loop
ax.annotate('', xy=(0.06,0.32), xytext=(0.90,0.32), arrowprops=dict(arrowstyle='->'))
ax.text(0.48, 0.22, 'feedback/update loop', ha='center')
ax.set_title('Classical-Quantum Hybrid Execution Workflow')
plt.tight_layout()
plt.show()
