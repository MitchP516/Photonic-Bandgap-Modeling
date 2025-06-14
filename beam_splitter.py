import meep as mp
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
cell_size = mp.Vector3(20, 20, 0)
resolution = 32
pml_layers = [mp.PML(1.0)]

# Geometry: Y-junction beam splitter
geometry = []
r = 0.2
eps = 12
for i in range(-10, 11):
    for j in range(-10, 11):
        if not (i == 0 and abs(j) <= 5) and not (i == 1 and j > 5) and not (i == -1 and j > 5):
            geometry.append(mp.Cylinder(radius=r, center=mp.Vector3(i, j), material=mp.Medium(epsilon=eps)))

# Source
sources = [mp.Source(mp.GaussianSource(frequency=0.15, fwidth=0.1),
                     component=mp.Ez,
                     center=mp.Vector3(0, 0))]

# Simulation
sim = mp.Simulation(cell_size=cell_size,
                    resolution=resolution,
                    geometry=geometry,
                    sources=sources,
                    boundary_layers=pml_layers)

# Flux monitors
flux1 = sim.add_flux(0.15, 0.1, 100, mp.FluxRegion(center=mp.Vector3(5, 2), size=mp.Vector3(0, 2)))
flux2 = sim.add_flux(0.15, 0.1, 100, mp.FluxRegion(center=mp.Vector3(-5, 2), size=mp.Vector3(0, 2)))

# Run
sim.run(until=200)
flux_data1 = mp.get_fluxes(flux1)
flux_data2 = mp.get_fluxes(flux2)
print(f"Flux in branch 1: {flux_data1[0]}")
print(f"Flux in branch 2: {flux_data2[0]}")

# Visualize
ez_data = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ez)
plt.imshow(ez_data.transpose(), cmap='RdBu')
plt.colorbar()
plt.title("Ez Field in Y-Junction Beam Splitter")
plt.savefig("beam_splitter_ez.png")
plt.show()
