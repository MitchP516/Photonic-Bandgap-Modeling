import meep as mp
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
cell_size = mp.Vector3(20, 20, 0)
resolution = 32
pml_layers = [mp.PML(1.0)]

# Geometry: Two waveguides for MZI-based AND gate
geometry = []
r = 0.2
eps = 12
for i in range(-10, 11):
    for j in range(-10, 11):
        if not (i == 0 and abs(j) <= 8) and not (i == 2 and abs(j) <= 8):
            geometry.append(mp.Cylinder(radius=r, center=mp.Vector3(i, j), material=mp.Medium(epsilon=eps)))

# Sources: Two inputs for AND gate
sources = [
    mp.Source(mp.GaussianSource(frequency=0.15, fwidth=0.1), component=mp.Ez, center=mp.Vector3(-8, 0)),  # Input A
    mp.Source(mp.GaussianSource(frequency=0.15, fwidth=0.1), component=mp.Ez, center=mp.Vector3(-8, 2))   # Input B
]

# Simulation
sim = mp.Simulation(cell_size=cell_size,
                    resolution=resolution,
                    geometry=geometry,
                    sources=sources,
                    boundary_layers=pml_layers)

# Flux monitor at output
flux_out = sim.add_flux(0.15, 0.1, 100, mp.FluxRegion(center=mp.Vector3(8, 0), size=mp.Vector3(0, 2)))

# Run
sim.run(until=200)
flux_data = mp.get_fluxes(flux_out)
print(f"Output flux: {flux_data[0]}")  # High flux = logic 1

# Visualize
ez_data = sim.get_array(center=mp.Vector3(), size=cell_size, component=mp.Ez)
plt.imshow(ez_data.transpose(), cmap='RdBu')
plt.colorbar()
plt.title("Ez Field in Photonic AND Gate")
plt.savefig("logic_gate_ez.png")
plt.show()
