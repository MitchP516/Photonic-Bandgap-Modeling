import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

# Draw beam splitter as diagonal line
ax.plot([-2, 2], [-2, 2], 'k-', linewidth=3, label='Beam Splitter')

# Paths
ax.plot([-10, 0], [0, 0], 'b--', label='Incoming Path')
ax.plot([0, 10], [0, 0], 'g--', label='Transmitted Path')
ax.plot([0, 0], [0, 10], 'r--', label='Reflected Path')
ax.legend()

# List of photons: each is a dict with 'x', 'y', 'vx', 'vy', 'split'
photons = []

scatter = ax.scatter([], [], s=20, color='yellow', label='Photons')

def init():
    scatter.set_offsets(np.empty((0,2)))
    return scatter,

def update(frame):
    # Add new photon every 5 frames
    if frame % 5 == 0:
        photons.append({'x': -10, 'y': random.uniform(-0.5, 0.5), 'vx': 0.2, 'vy': 0, 'split': False})

    # Update positions
    to_remove = []
    offsets = []
    for p in photons:
        p['x'] += p['vx']
        p['y'] += p['vy']
        if p['x'] >= 0 and not p['split']:
            p['split'] = True
            if random.random() < 0.5:
                # transmit: continue right
                pass
            else:
                # reflect: go up
                p['vx'] = 0
                p['vy'] = 0.2
        offsets.append([p['x'], p['y']])
        if p['x'] > 10 or p['y'] > 10:
            to_remove.append(p)
    for p in to_remove:
        photons.remove(p)
    scatter.set_offsets(offsets)
    return scatter,

ani = FuncAnimation(fig, update, frames=500, init_func=init, interval=50, blit=True)
plt.title('Simulation of Photonic Beam Splitting')
plt.show()
