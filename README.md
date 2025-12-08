# 🌲 Forest Fire Simulation

A Python-based forest fire simulation built as part of a university project in Computer Simulations.  
The simulation models how fire spreads across a 2D forest grid, using probabilistic rules and cellular automata techniques.

---

## 🚀 Project Status

The project is currently **in development**.  
The following core module has been completed:

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

This module ensures a consistent and fully functional starting point for the future fire-spread dynamics.

---

## 🗂 Project Structure

```
Forest_Fire_Simulation/
│
├── src/
│   └── forest_fire/
│       ├── forest.py        # forest initialization logic
│       ├── states.py        # definitions of cell states
│
├── run.py                   # entry point for running the simulation
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Running the project

After installing dependencies:

```bash
pip install -r requirements.txt
```

Run the test script:

```bash
python run.py
```

This will generate and print the initial forest grid.

---

## 🔧 Requirements

- Python 3.10+  
- NumPy  
- (Matplotlib will be added later for visualizations)

---

## 📌 Next Steps (Planned)

These components will be developed next:

### 🔥 Fire Spread Logic
`spread_fire()` function that updates the forest state based on fire propagation rules.

### 🔁 Simulation Loop
`simulate()` function running the cellular automaton step by step.

### 🎨 Visualization
Heatmaps / animations using Matplotlib to show how the fire evolves over time.

### 📄 Report
A detailed technical report describing:
- the model  
- assumptions  
- results  
- and visualizations  

---

## 📚 Academic Context

This project is created for the **Computer Simulations** course.  
It implements concepts such as cellular automata, probabilistic transitions, and environment modeling.

---

## 👤 Author

Kamil Matus  
Forest Fire Simulation — 2025/2026

