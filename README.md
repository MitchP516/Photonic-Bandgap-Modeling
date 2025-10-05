This repository contains a series of Python scripts that simulate various photonic phenomena using Matplotlib for visualization and NumPy for numerical computations. Each script provides an animated simulation of a specific photonic concept, including beam splitting, band structure, logic gates, and waveguides. Below are details for each program created during this session.

Programs Included

1. Photonic Beam Splitting Simulation





File: beam_splitting.py



Description: Simulates photons passing through a 50/50 beam splitter. Photons approach from the left and randomly split into transmitted or reflected paths with equal probability.



Features: Random photon generation, visual paths, and animation of splitting behavior.



Dependencies: matplotlib, numpy



How to Run: Execute python beam_splitting.py in an environment with a GUI backend (e.g., Jupyter Notebook).

2. Photonic Band Structure Simulation





File: band_structure.py



Description: Animates the band structure of a 1D photonic crystal with alternating layers of different refractive indices.



Features: Progressive plotting of allowed bands, transfer matrix method, and frequency sweep.



Dependencies: matplotlib, numpy



How to Run: Execute python band_structure.py in an environment with a GUI backend.

3. Photonic AND Logic Gate Simulation





File: logic_gate.py



Description: Simulates a photonic AND gate where an output photon is generated only if photons from two inputs arrive simultaneously.



Features: Random input photon generation, coincidence detection, and output visualization.



Dependencies: matplotlib, numpy



How to Run: Execute python logic_gate.py in an environment with a GUI backend.

4. Photonic Waveguide Simulation





File: waveguide.py



Description: Animates the propagation of an electromagnetic wave in a slab waveguide with color shading to represent field amplitude.



Features: Mode profile calculation, paraxial wave propagation, and real-time field visualization.



Dependencies: matplotlib, numpy



How to Run: Execute python waveguide.py in an environment with a GUI backend.

Installation





Ensure you have Python 3.x installed.



Install required packages:

pip install matplotlib numpy



Save each script with the suggested filenames in the same directory.

Usage





Run each script individually to view the corresponding animation.



Adjust parameters (e.g., number of frames, speeds, refractive indices) within the scripts as needed.



Use a Jupyter Notebook or an IDE with Matplotlib support for best results.

Notes





These simulations use simplified models for educational purposes. Real-world photonic systems may require more complex methods (e.g., FDTD).



Errors like shape mismatches or unhashable types can occur; refer to the session context for fixes if needed.



The animations are best viewed in environments supporting interactive plots (e.g., Jupyter with %matplotlib notebook or a desktop Python environment).

License

This code is provided for educational use. Feel free to modify and distribute, but please retain this README.
