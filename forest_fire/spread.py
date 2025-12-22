"""
spread.py

Contains the function responsible for simulating how fire spreads within the forest grid.
"""

import numpy as np
from .states import TREE, BURNING, BURNED

def spread_fire(forest, burned_age, ignition_prob=0.5, wind_direction = None, ps = 1e-4, regrowth_time = 10):

    # Step 1: Identify burning cells
    burning_mask = (forest == BURNING)
    
    # Step 2: Compute burning neighbours (8-neighbourhood)
    burning_neighbors = np.zeros_like(forest, dtype = bool)
    
    up = np.zeros_like(forest, dtype=bool)
    down = np.zeros_like(forest, dtype=bool)
    right = np.zeros_like(forest, dtype=bool)
    left = np.zeros_like(forest, dtype=bool)
    up_right = np.zeros_like(forest, dtype=bool)
    up_left = np.zeros_like(forest, dtype=bool)
    down_right = np.zeros_like(forest, dtype=bool)
    down_left = np.zeros_like(forest, dtype=bool)
    
    up[:-1, :] = burning_mask[1:, :]
    down[1:, :] = burning_mask[:-1, :]
    right[:, 1:] = burning_mask[:, :-1]
    left[:, :-1] = burning_mask[:, 1:]
    up_right[:-1, 1:] = burning_mask[1:, :-1]
    up_left[:-1, :-1] = burning_mask[1:, 1:]
    down_right[1:, 1:] = burning_mask[:-1, :-1]
    down_left[1:, :-1] = burning_mask[:-1, 1:]
    
    burning_neighbors |= up
    burning_neighbors |= down
    burning_neighbors |= left
    burning_neighbors |= right
    burning_neighbors |= up_right
    burning_neighbors |= up_left
    burning_neighbors |= down_right
    burning_neighbors |= down_left

    # Step 3: Adjust ignition probabilities based on wind direction 
    if wind_direction is not None:
        wind_map = {
            "N": {
                "with": ["up", "up_right", "up_left"],
                "against": ["down", "down_right", "down_left"],
                "neutral": ["left", "right"]
            },
            "S": {
                "with": ["down", "down_right", "down_left"],
                "against": ["up", "up_right", "up_left"],
                "neutral": ["left", "right"]
            },
            "E": {
                "with": ["right", "up_right", "down_right"],
                "against": ["left", "up_left", "down_left"],
                "neutral": ["up", "down"]
            },
            "W": {
                "with": ["left", "up_left", "down_left"],
                "against": ["right", "up_right", "down_right"],
                "neutral": ["up", "down"]
            }
        }

        with_wind = min(1.0, ignition_prob * 2)      
        against_wind = ignition_prob *0.5
        neutral_wind = ignition_prob
    
    # Step 4: Determine spontaneous ignition (self-ignition ps) 
    tree_ps_mask = (forest == TREE)
    random_ps_values = np.random.random(forest.shape)
    ps_ignition_mask = random_ps_values < ps
    spontaneous_fire_mask = tree_ps_mask & ps_ignition_mask
    
    # Step 5: Determine which TREE cells ignite 
    tree_mask = (forest == TREE)
    candidate_mask = tree_mask & burning_neighbors
    local_p = np.zeros_like(forest, dtype = float)
       
    if wind_direction is not None:
        direction_masks = {
            "up": up,
            "down": down,
            "left": left,
            "right": right,
            "up_left": up_left,
            "up_right": up_right,
            "down_left": down_left,
            "down_right": down_right
        }
        
        wind_groups = wind_map[wind_direction]
        
        for d in wind_groups["with"]:
            mask = direction_masks[d]
            local_p[mask & candidate_mask] = with_wind
            
        for d in wind_groups["neutral"]:
            mask = direction_masks[d]
            local_p[(mask & candidate_mask) & (local_p == 0)] = neutral_wind
        
        for d in wind_groups["against"]:
            mask = direction_masks[d]
            local_p[(mask & candidate_mask) & (local_p == 0)] = against_wind
    else:
        local_p[candidate_mask] = ignition_prob
    
    random_values = np.random.random(forest.shape)
    random_mask = (random_values < local_p)
    ignition_mask = candidate_mask & random_mask
    final_ignition_mask = ignition_mask | spontaneous_fire_mask
    forest_next = forest.copy()
    forest_next[final_ignition_mask] = BURNING
    
    # Step 6: Update BURNING -> BURNED 
    forest_next[burning_mask] = BURNED

    # Step 7: Regenerate burned trees after k steps 
    regener_mask = ((burned_age >= regrowth_time) & (forest_next == BURNED))
    forest_next[regener_mask] = TREE
    burned_age[regener_mask] = 0
    
    # Step 8: Update burned_age array 
    burned_age[(forest_next == BURNED)] += 1
    burned_age[(forest_next != BURNED)] = 0

    # Step 9: Return new forest and burned_age 
    return forest_next, burned_age
