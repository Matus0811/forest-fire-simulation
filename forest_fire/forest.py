"""
forest.py

Contains functions responsible for creating and initializing the forest grid
used in the forest fire simulation. This includes generating trees, water,
and selecting an initial burning tree.
"""

import numpy as np
from .states import EMPTY, TREE, BURNING, WATER

def init_forest(size = (50,50), tree_density = 0.6, water_density = 0.05, seed = None):
    # Step 1: Set random seed if provided
    rows, columns = size
    if seed is not None:
        np.random.seed(seed)
        
    # Step 2: Create an empty grid
    forest = np.full((rows, columns), EMPTY)
    
    # Step 3: Randomly place water cells
    random_array_water = np.random.rand(rows,columns)
    water_mask = random_array_water < water_density
    forest[water_mask] = WATER
    
    # Step 4: Randomly place tree cells
    random_array_tree = np.random.rand(rows,columns)
    tree_mask = random_array_tree < tree_density
    available_mask = (forest == EMPTY)
    final_tree_mask = tree_mask & available_mask
    forest[final_tree_mask] = TREE
    
    # Step 5: Initialize burned_age array
    burned_age = np.zeros((rows,columns), dtype = int)
    
    # Step 6: Select a random TREE to ignite
    tree_positions = (forest == TREE)
    tree_rows, tree_columns = np.where(tree_positions)
    i = np.random.choice(len(tree_rows))
    r = tree_rows[i]
    c = tree_columns[i]
    forest[r,c] = BURNING
    
    # Step 7: Return forest and burned_age
    return forest, burned_age
