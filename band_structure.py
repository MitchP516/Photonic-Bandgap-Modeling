import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
c = 1.0  # speed of light (normalized units)
a = 1.0  # lattice period
d1 = 0.5 * a  # thickness of layer 1
d2 = 0.5 * a  # thickness of layer 2
n1 = 1.0  # refractive index of layer 1 (e.g., air)
n2 = 3.5  # refractive index of layer 2 (e.g., GaAs-like)
eta1 = n1  # admittance (for TM polarization at normal incidence)
eta2 = n2

# Function to compute the transfer matrix for a single layer
def layer_matrix(delta, eta):
    return np.array([
        [np.cos(delta), 1j * np.sin(delta) / eta],
        [1j * eta * np.sin(delta), np.cos(delta)]
    ])

# Function to compute the transfer matrix for one period
def transfer_matrix(omega):
    k1 = omega * n1 / c
    k2 = omega * n2 / c
    delta1 = k1 * d1
    delta2 = k2 * d2
    M1 = layer_matrix(delta1, eta1)
    M2 = layer_matrix(delta2, eta2)
    M = np.matmul(M1, M2)  # Assuming layer 1 followed by layer 2
    return M

# Function to compute cos(K a)
def cos_Ka(omega):
    M = transfer_matrix(omega)
    return np.real((M[0, 0] + M[1, 1]) / 2)  # Real part for lossless system

# Setup for band structure calculation
max_freq = 4.0  # Maximum normalized frequency \omega a / (2 \pi c)
num_points = 10000  # Number of omega points for dense sampling
omegas = np.linspace(0.001, max_freq * 2 * np.pi, num_points)  # Avoid omega=0 singularity

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(0, np.pi / a)
ax.set_ylim(0, max_freq)
ax.set_xlabel('Wavevector K a / \pi')
ax.set_ylabel('Frequency \omega a / (2 \pi c)')
scatter = ax.scatter([], [], s=1, color='blue')

def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

def update(frame):
    # Cumulative up to current frame
    current_omegas = omegas[:frame + 1]
    Ks = []
    freqs = []
    for omega in current_omegas:
        cos = cos_Ka(omega)
        if np.abs(cos) <= 1:
            Ka = np.arccos(np.clip(cos, -1.0, 1.0))
            K = Ka / a
            freq = omega / (2 * np.pi)
            Ks.append(K / np.pi)  # Normalize K by / \pi
            freqs.append(freq)
    offsets = np.c_[Ks, freqs]
    scatter.set_offsets(offsets)
    return scatter,

ani = FuncAnimation(fig, update, frames=num_points, init_func=init, interval=1, blit=True)
plt.title('Animated Simulation of 1D Photonic Band Structure')
plt.show()
