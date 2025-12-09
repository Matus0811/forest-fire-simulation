"""
run.py

Simple test runner for the forest fire simulation.
Used for debugging individual steps of the algorithm (e.g., Step 2).
"""

from forest_fire.forest import init_forest
from forest_fire.spread import spread_fire

def main():
    # Create a small forest for debugging
    forest, burned_age = init_forest(size=(5, 5), seed=0)

    print("Initial forest:")
    print(forest)
    print()

    # Run one step of fire spreading
    new_forest, new_burned_age = spread_fire(forest, burned_age)

    print("Forest after spread_fire():")
    print(new_forest)
    print()

    # Since Step 2 prints burning_neighbors internally,
    # you will see its values when running the program.

if __name__ == "__main__":
    main()

