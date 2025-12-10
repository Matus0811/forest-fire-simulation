"""
spread.py

Contains the function responsible for simulating how fire spreads within the forest grid.
"""

import numpy as np
from .states import TREE, BURNING, BURNED

def spread_fire(forest, burned_age, ignition_prob=1.0, wind_direction = None):

    # Step 1: Identify burning cells
    burning_mask = (forest == BURNING)
    
    # Step 2: Compute burning neighbours (8-neighbourhood)
    burning_neighbors = np.zeros_like(forest, dtype = bool)
    up = burning_mask[1:,:]
    down = burning_mask[:-1,:]
    right = burning_mask[:,:-1]
    left = burning_mask[:,1:]
    up_right = burning_mask[1:,:-1]
    up_left = burning_mask[1:,1:]
    down_right = burning_mask[:-1,:-1]
    down_left = burning_mask[:-1,1:]
    
    burning_neighbors[:-1,:] |= up
    burning_neighbors[1:,:] |= down
    burning_neighbors[:,1:] |= right
    burning_neighbors[:,:-1] |= left
    burning_neighbors[:-1,1:] |= up_right
    burning_neighbors[:-1,:-1] |= up_left
    burning_neighbors[1:,1:] |= down_right
    burning_neighbors[1:,:-1] |= down_left

    # Step 3: Adjust ignition probabilities based on wind direction 
    if wind_direction is not None:
        wind_map = {
            "N": {
                "with": [up, up_right, up_left],
                "against": [down, down_right, down_left],
                "neutral": [left,right]
            },
            "S": {
                "with": [down, down_right, down_left],
                "against": [up, up_right, up_left],
                "neutral": [left,right]
            },
            "E": {
                "with": [right, up_right, down_right],
                "against": [left, up_left, down_left],
                "neutral": [up, down]
            },
            "W": {
                "with": [left, up_left, down_left],
                "against": [right, up_right, down_right],
                "neutral": [up, down]
            }
        }
        
    
    # Step 4: Determine spontaneous ignition (self-ignition ps) 
    

    # Step 5: Determine which TREE cells ignite 
    tree_mask = (forest == TREE)
    candidate_mask = tree_mask & burning_neighbors
    random_values = np.random.random(forest.shape)
    random_mask = (random_values < ignition_prob)
    ignition_mask = candidate_mask & random_mask
    forest_next = forest.copy()
    forest_next[ignition_mask] = BURNING
    
    # Step 6: Update BURNING -> BURNED 
    forest_next[burning_mask] = BURNED

    # Step 7: Regenerate burned trees after k steps 
    

    # Step 8: Update burned_age array 
    burned_age[:] = 0
    burned_mask = (forest_next == BURNED)
    burned_age[burned_mask] += 1

    # Step 9: Return new forest and burned_age 
    return forest_next, burned_age
