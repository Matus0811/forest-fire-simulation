# 🌲 Forest Fire Simulation

A Python-based forest fire simulation built as part of a university project in **Computer Simulations**.
The simulation models how fire spreads across a 2D forest grid using probabilistic rules, cellular automata techniques, and dynamic environmental factors such as wind and vegetation regrowth.

---

## 🚀 Project Status

The project is **complete**.
All core components of the simulation, including fire spread logic, dynamic wind influence, visualization, and result export, have been fully implemented.

---

## 🌱 Implemented Features

### ✔ Forest Initialization (`init_forest`)
Responsible for preparing the full initial environment for the simulation:

- Creates an empty forest grid of configurable size
- Randomly places **WATER** cells based on `water_density`
- Randomly places **TREE** cells based on `tree_density`
- Ensures TREE cells never overwrite WATER
- Initializes a parallel `burned_age` matrix
- Selects one random TREE and **ignites it** (`BURNING` state)

This module ensures a consistent and fully functional starting point for the fire-spread dynamics.

---

### ✔ Fire Spread Logic (`spread_fire`)
Implements the cellular automaton rules governing fire propagation:

- Probabilistic fire spread using an 8-neighbourhood
- Fire spreads only to adjacent **TREE** cells
- **WATER** cells completely block fire propagation
- Support for **spontaneous ignition** with configurable probability
- Burning cells transition to a **BURNED** state

---

### ✔ Dynamic Wind Influence
Environmental wind conditions affecting fire spread:

- Wind directions supported: **N, S, E, W**
- Wind direction modifies ignition probability
- Wind direction changes **dynamically every fixed number of iterations**
- Wind history is stored for each simulation step
- Current wind direction is displayed directly in the visualization

---

### ✔ Vegetation Regrowth
Post-fire regeneration mechanism:

- Burned cells remain in the **BURNED** state for a configurable number of steps
- Trees automatically regenerate after the regrowth period

---

### ✔ Simulation Loop (`simulate_fire`)
Controls the time evolution of the system:

- Event-based simulation loop
- Simulation runs until all fires extinguish
- Additional “quiet steps” window prevents premature termination due to spontaneous ignition
- Full history of forest states is collected for visualization

---

### ✔ Visualization and Output
Visual representation of the simulation:

- Visualization implemented using **Matplotlib**
- Discrete color mapping for all forest states
- Animated visualization of fire spread over time
- Export of results as a **GIF animation**
- Animation displays:
  - iteration number
  - current wind direction

**Simulation Preview:**

![Forest Fire Simulation Preview](outputs/forest_fire_simulation.gif)

---

## 🗂 Project Structure

```text
Forest_Fire_Simulation/
│
├── forest_fire/
│   ├── forest.py      # forest initialization logic
│   ├── spread.py      # fire spread rules
│   ├── simulate.py    # simulation controller and time evolution
│   ├── visualize.py   # visualization and animation export
│   ├── states.py      # definitions of cell states
│   └── __init__.py
│
├── outputs/
│   └── forest_fire_simulation.gif
│
├── run.py             # main entry point for running the simulation
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Running the Project

After installing dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python run.py
```

This will:
1. execute the full simulation loop,
2. generate an animated visualization of the fire spread,
3. save the animation to the `outputs/` directory.

---

## 🔧 Requirements

- Python 3.9+
- NumPy
- Matplotlib
- Pillow

---

## 📚 Academic Context

This project is created for the **Computer Simulations** course.
It demonstrates concepts such as:
- cellular automata
- probabilistic state transitions
- environmental modeling
- dynamic system simulation and visualization

---

## 👤 Author

**Kamil Matusiak**
Forest Fire Simulation — Academic Year 2025/2026