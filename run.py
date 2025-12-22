"""
run.py

Simple test runner for the forest fire simulation.
Tests full simulation loop with wind, spontaneous ignition
and termination condition.
"""

from forest_fire.simulate import simulate_fire


def main():
    # --- Simulation parameters ---
    size = (10, 10)
    tree_density = 0.6
    water_density = 0.05

    ignition_prob = 0.5
    wind_direction = "N"      # try: "N", "S", "E", "W", None
    ps = 1e-2                 # higher than normal to SEE spontaneous fires
    regrowth_time = 3
    quiet_steps_limit = 5     # short silence window for testing
    seed = 1

    # --- Run full simulation ---
    frames = simulate_fire(
        size=size,
        tree_density=tree_density,
        water_density=water_density,
        ignition_prob=ignition_prob,
        wind_direction=wind_direction,
        ps=ps,
        regrowth_time=regrowth_time,
        seed=seed,
        quiet_steps_limit=quiet_steps_limit
    )

    # --- Print results ---
    print(f"Simulation finished after {len(frames) - 1} steps")
    print("-" * 40)

    print("Initial forest:")
    print(frames[0])
    print("-" * 40)

    print("Final forest:")
    print(frames[-1])
    print("-" * 40)


if __name__ == "__main__":
    main()
