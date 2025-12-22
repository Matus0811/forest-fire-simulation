"""
simulate.py

Controls the time evolution of the forest fire simulation.
Responsible only for running the simulation loop and
collecting successive forest states.
"""

from forest_fire.forest import init_forest
from forest_fire.spread import spread_fire
from .states import BURNING

def simulate_fire(size = (50, 50), tree_density = 0.6, water_density = 0.05, ignition_prob = 0.5, wind_direction = None, ps = 1e-4, regrowth_time = 10, seed = None, quiet_steps_limit = 10):
    # Step 1: Initialize the forest and burned_age
    forest, burned_age = init_forest(size, tree_density, water_density, seed)
    
    # Step 2: Prepare container for simulation frames
    frames = []
    frames.append(forest.copy())
    
    # Step 3: Main simulation loop
    step = 0
    fire_stop = 0
    burns = (forest == BURNING)
    while(burns.any() or fire_stop < quiet_steps_limit):
        new_forest, new_burned_age = spread_fire(forest, burned_age, ignition_prob, wind_direction, ps, regrowth_time)
        forest = new_forest
        burned_age = new_burned_age
        burns =(forest == BURNING)
        if burns.any(): fire_stop = 0
        else: fire_stop += 1
        frames.append(forest.copy()) 
        step += 1
    
    # Step 4: Return simulation results
    return frames
