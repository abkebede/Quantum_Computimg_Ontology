"""Simplified Bloch-vector trajectory for a gate sequence."""
import numpy as np
import matplotlib.pyplot as plt

# Represent a simple path: |0> north pole -> H-like equator -> phase rotation -> X-like rotation
points = np.array([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, -1],
])

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
# sphere wireframe
u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 25)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))
ax.plot_wireframe(x, y, z, linewidth=0.3, alpha=0.4)
ax.plot(points[:,0], points[:,1], points[:,2], marker='o')
for label, p in zip(['|0>', 'after H', 'after Rz', 'after Rx'], points):
    ax.text(p[0], p[1], p[2], label)
ax.set_title('Simplified Bloch-Sphere Gate Sequence')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.tight_layout()
plt.show()
