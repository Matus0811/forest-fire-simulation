"""
run.py

Main entry point for the forest fire simulation project.
Runs the simulation with selected parameters and saves
the visualization of the results as an animation file.
"""

from forest_fire.simulate import simulate_fire
from forest_fire.visualize import save_simulation_animation


def main():
    # --- Simulation configuration ---
    size = (50, 50)
    tree_density = 0.6
    water_density = 0.05

    ignition_prob = 0.5
    wind_direction = "N"      # "N", "S", "E", "W" or None
    ps = 1e-4                 # spontaneous ignition probability
    regrowth_time = 10
    quiet_steps_limit = 10
    seed = 42
    wind_change_interval = 5

    # --- Run simulation ---
    frames, winds = simulate_fire(
        size=size,
        tree_density=tree_density,
        water_density=water_density,
        ignition_prob=ignition_prob,
        wind_direction=wind_direction,
        ps=ps,
        regrowth_time=regrowth_time,
        seed=seed,
        quiet_steps_limit=quiet_steps_limit,
        wind_change_interval=wind_change_interval
    )

    # --- Save visualization ---
    output_path = "outputs/forest_fire_simulation.gif"
    save_simulation_animation(frames, winds, output_path, fps=8)

    print("Simulation completed successfully.")
    print(f"Total iterations: {len(frames) - 1}")
    print(f"Visualization saved to: {output_path}")


if __name__ == "__main__":
    main()
