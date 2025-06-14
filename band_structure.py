from meep import mpb
import meep as mp
import matplotlib.pyplot as plt

# Define 2D square lattice
k_points = [mp.Vector3(), mp.Vector3(0.5, 0), mp.Vector3(0.5, 0.5), mp.Vector3()]  # High-symmetry points
geometry_lattice = mp.Lattice(size=mp.Vector3(1, 1))
ms = mpb.ModeSolver(
    geometry_lattice=geometry_lattice,
    geometry=[mp.Cylinder(0.2, material=mp.Medium(epsilon=12))],
    k_points=k_points,
    resolution=32,
    num_bands=8
)

# Run for TM modes
ms.run_tm()

# Plotting handled by MPB's default output; save manually if needed
