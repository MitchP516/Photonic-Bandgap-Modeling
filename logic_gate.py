import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
from matplotlib.patches import Rectangle

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')

# Draw paths
ax.plot([-10, 0], [-2, -2], 'b--', label='Input A')
ax.plot([-10, 0], [2, 2], 'g--', label='Input B')
ax.plot([0, 10], [0, 0], 'r--', label='Output')
ax.add_patch(Rectangle((-1, -3), 2, 6, fill=False, edgecolor='k', linewidth=2, label='AND Gate'))
ax.legend()

# List of photons: each is a dict with 'x', 'y', 'vx', 'type' ('A','B','out'), 'processed'
photons = []

scatter = ax.scatter([], [], s=20)

def init():
    scatter.set_offsets(np.empty((0,2)))
    return scatter,

def update(frame):
    # Add new photons randomly to inputs
    if frame % 5 == 0:
        if random.random() < 0.3:
            photons.append({'x': -10, 'y': -2 + random.uniform(-0.2, 0.2), 'vx': 0.2, 'type': 'A', 'processed': False})
        if random.random() < 0.3:
            photons.append({'x': -10, 'y': 2 + random.uniform(-0.2, 0.2), 'vx': 0.2, 'type': 'B', 'processed': False})

    # Update positions
    to_remove = []
    for p in photons:
        p['x'] += p['vx']
        if p['type'] == 'out' and p['x'] > 10:
            to_remove.append(p)
        elif p['x'] >= 0 and not p['processed'] and p['type'] != 'out':
            p['processed'] = True
            match = None
            target_type = 'B' if p['type'] == 'A' else 'A'
            for q in photons:
                if q['type'] == target_type and abs(q['x'] - p['x']) < 0.5 and not q['processed']:
                    match = q
                    break
            if match:
                match['processed'] = True
                # Create output photon
                photons.append({'x': 0, 'y': random.uniform(-0.2, 0.2), 'vx': 0.2, 'type': 'out', 'processed': False})
                to_remove.append(p)
                to_remove.append(match)
            else:
                # No match, absorbed
                to_remove.append(p)

    # Remove processed/absorbed/out-of-bound photons
    for r in to_remove:
        photons.remove(r)

    # Update scatter
    if photons:
        offsets = np.array([[p['x'], p['y']] for p in photons])
        colors = ['blue' if p['type'] == 'A' else 'green' if p['type'] == 'B' else 'red' for p in photons]
        scatter.set_offsets(offsets)
        scatter.set_facecolors(colors)
    else:
        scatter.set_offsets(np.empty((0,2)))

    return scatter,

ani = FuncAnimation(fig, update, frames=500, init_func=init, interval=50, blit=True)
plt.title('Simulation of Photonic AND Logic Gate')
plt.show()
