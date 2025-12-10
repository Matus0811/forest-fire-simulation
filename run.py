"""
run.py

Simple test runner for the forest fire simulation.
Used for debugging individual steps of the algorithm 
"""

from forest_fire.forest import init_forest
from forest_fire.spread import spread_fire

def main():
    forest, burned_age = init_forest(size=(10, 10), seed=0)

    print("Initial forest:")
    print(forest)
    print()

    forest_next, burned_age_next = spread_fire(forest, burned_age)

    print("After one spread step:")
    print(forest_next)
    print()

    print("Burned age:")
    print(burned_age_next)

if __name__ == "__main__":
    main()


