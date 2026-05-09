# SPHY Visualizer

**Interactive 3D Visualizer for H₂O Dissociation Simulation with Cryptographic Audit**

## 📋 What does this visualizer do?

The `sphy_visualizer.py` loads a pre-generated sequence of frames and renders a **real-time 3D animation** of the water molecule (H₂O) dissociation simulation.

### Key Features:

- Real-time 3D visualization of the oxygen atom and two hydrogen atoms moving apart.
- Dynamic rendering of the surrounding S(Φ) energy field.
- Live cryptographic audit display:
  - SHA-256 hash for each individual frame
  - System stability percentage
  - Resonance factor
  - Hydrogen atoms distance
- Visual alert when dissociation is detected.
- Clean scientific HUD (Heads-Up Display) interface.

> This visualizer **does not generate** the simulation data — it only replays the pre-computed frames.

## 📁 Required File

- **`sphy_frames.parquet`**  
  Must be placed in the same directory as the script.

This Parquet file contains all simulation frames with their respective SHA-256 signatures.

## 🛠 Requirements

### Main Dependencies:

- **py5** — Creative coding library (Processing for Python)
- **pandas** — For reading Parquet files

### Installation:

```bash
pip install py5 pandas pyarrow

pyarrow is recommended for faster Parquet file loading.How to UseMake sure the file sphy_frames.parquet is in the same folder.
Run the visualizer:

bash

python sphy_visualizer.py

The animation will start automatically and loop when finished.

Made by:
Deywe Okabe
Harpia Quantum DeeptechPronto!
Você pode copiar e colar diretamente no arquivo README.md.Quer que eu inclua também uma versão curta para o GitHub ou adicione badges?

