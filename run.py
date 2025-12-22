"""
run.py

Simple test runner for the forest fire simulation.
Tests fire spread, wind influence, spontaneous ignition
and forest regeneration.
"""

from forest_fire.forest import init_forest
from forest_fire.spread import spread_fire


def main():
    # --- Simulation parameters ---
    size = (10, 10)
    steps = 8
    ignition_prob = 0.5
    wind_direction = "N"     # test wind (try: N, S, E, W, None)
    ps = 1e-2                # higher than normal so we can SEE spontaneous fires
    regrowth_time = 3        # small so regeneration happens quickly

    # --- Initialize forest ---
    forest, burned_age = init_forest(size=size, seed=0)

    print("Initial forest:")
    print(forest)
    print("-" * 40)

    # --- Run simulation ---
    for step in range(steps):
        forest, burned_age = spread_fire(
            forest,
            burned_age,
            ignition_prob=ignition_prob,
            wind_direction=wind_direction,
            ps=ps,
            regrowth_time=regrowth_time
        )

        print(f"Step {step + 1}:")
        print(forest)
        print("Burned age:")
        print(burned_age)
        print("-" * 40)


if __name__ == "__main__":
    main()
