"""
spread.py

Contains the function responsible for simulating how fire spreads within the forest grid.
"""

import numpy as np
from .states import EMPTY, TREE, BURNING, BURNED, WATER

def spread_fire(forest, burned_age, ignition_prob=1.0):
    # Step 1: Identify burning cells
    burning_mask = (forest == BURNING)
    # Step 2: Compute burning neighbours (8-neighbourhood)
    burning_neighbors = np.zeros_like(forest, dtype = bool)
    up = burning_mask[1:,:]
    down = burning_mask[:-1,:]
    right = burning_mask[:,:-1]
    left = burning_mask[:,1:]
    up_rigt = burning_mask[1:,:-1]
    up_left = burning_mask[1:,1:]
    down_right = burning_mask[:-1,:-1]
    down_left = burning_mask[:-1,1:]
    
    burning_neighbors[:-1,:] |= up
    burning_neighbors[1:,:] |= down
    burning_neighbors[:,1:] |= right
    burning_neighbors[:,:-1] |= left
    burning_neighbors[:-1,1:] |= up_rigt
    burning_neighbors[:-1,:-1] |= up_left
    burning_neighbors[1:,1:] |= down_right
    burning_neighbors[1:,:-1] |= down_left
    # Step 3: Determine which TREE cells ignite
    # Step 4: Update BURNING -> BURNED
    # Step 5: Update burned_age
    # Step 6: Return new forest and burned_age
    return forest, burned_age
