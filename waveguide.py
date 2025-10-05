import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize

# Parameters
L = 20.0  # Length of waveguide
W = 5.0   # Half-width for display
d = 2.0   # Waveguide core thickness (from -d/2 to d/2)
Nx = 200  # Grid points in x
Ny = 100  # Grid points in y
x = np.linspace(0, L, Nx)
y = np.linspace(-W, W, Ny)
X, Y = np.meshgrid(x, y)

# Wave parameters
k0 = 2 * np.pi  # Free space wavevector (normalized)
n_core = 3.5    # Refractive index of core
n_clad = 1.0    # Refractive index of cladding
beta = k0 * np.sqrt((n_core**2 + n_clad**2)/2)  # Approximate propagation constant
m = 0           # Mode number (0 for fundamental)
ky = m * np.pi / d
kz_core = np.sqrt(k0**2 * n_core**2 - beta**2 + ky**2)  # Simplified

# Time parameters
omega = k0  # Normalized frequency
t_steps = 100
dt = 0.1

# Mode profile function (simple even mode for slab waveguide)
def mode_profile(y):
    core_mask = np.abs(y) <= d/2
    profile = np.zeros_like(y)
    profile[core_mask] = np.cos(ky * y[core_mask])
    profile[~core_mask] = np.cos(ky * d/2) * np.exp(-np.abs(ky) * (np.abs(y[~core_mask]) - d/2))
    return profile / np.max(np.abs(profile))  # Normalize

# Precompute y-profile
profile_y = mode_profile(y)

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(-W, W)
ax.set_xlabel('Propagation Direction (x)')
ax.set_ylabel('Transverse Direction (y)')
# Draw waveguide boundaries
ax.axhline(-d/2, color='white', linestyle='--')
ax.axhline(d/2, color='white', linestyle='--')

# Initial field: real part for visualization
field = np.real(np.outer(np.ones(Nx), profile_y) * np.exp(1j * (beta * X.T - omega * 0)))
im = ax.pcolormesh(X, Y, field.T, cmap='RdBu', shading='auto', norm=Normalize(-1, 1))
fig.colorbar(im, ax=ax, label='Field Amplitude')

def update(frame):
    t = frame * dt
    # Create 2D field by broadcasting profile_y across x
    field_2d = np.outer(np.ones(Nx), profile_y)  # Shape (Nx, Ny) = (200, 100)
    # Compute the phase term for the entire grid, matching X's shape
    phase = 1j * (beta * X.T - omega * t)  # Transpose X to (Nx, Ny) = (200, 100)
    # Apply the mode profile and phase
    field = np.real(field_2d * np.exp(phase))
    im.set_array(field.T.ravel())  # Transpose back for pcolormesh
    return im,

ani = FuncAnimation(fig, update, frames=t_steps, interval=50, blit=True)
plt.title('Animated Simulation of Wave Propagation in a Photonic Slab Waveguide')
plt.show()
