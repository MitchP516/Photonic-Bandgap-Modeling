import meep as mp
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
cell_size = mp.Vector3(20, 20, 0)  # 2D simulation (z=0)
resolution = 32  # pixels per unit length
pml_layers = [mp.PML(1.0)]  # Perfectly matched layers for boundaries

# Photonic crystal: square lattice of dielectric rods
geometry = []
r = 0.2  # rod radius
eps = 12  # dielectric constant (e.g., silicon)
for i in range(-10, 11):
    for j in range(-10, 11):
        if i != 0:  # Remove central row to create waveguide
            geometry.append(mp.Cylinder(radius=r, center=mp.Vector3(i, j), material=mp.Medium(epsilon=eps)))

# Source: Gaussian pulse at center
sources = [mp.Source(mp.GaussianSource(frequency=0.15, fwidth=0.1),
                     component=mp.Ez,
                     center=mp.Vector3(0, 0))]

# Simulation
sim = mp.Simulation(cell_size=cell_size,
                    resolution=resolution,
                    geometry=geometry,
                    sources=sources,
                    boundary_layers=pml_layers)

# Run and visualize
sim.run(until=200)
ez_data = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ez)
plt.imshow(ez_data.transpose(), cmap='RdBu')
plt.colorbar()
plt.title("Ez Field in Photonic Crystal Waveguide")
plt.savefig("waveguide_ez.png")
plt.show()
