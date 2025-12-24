"""
visualize.py

Contains functions responsible for visualizing the forest fire simulation.
The module allows saving successive simulation states as an animation file.
"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap as lc
from matplotlib.animation import FuncAnimation, PillowWriter

from .states import EMPTY, TREE, BURNING, BURNED, WATER


def save_simulation_animation(frames, winds, output_path, fps=10):
    # Step 1: Prepare color map for forest states
    colors = [
        "#c2b280",  # EMPTY
        "#1b7f1b",  # TREE
        "#d32f2f",  # BURNING
        "#424242",  # BURNED
        "#1565c0"   # WATER
    ]   
    cmap = lc(colors)

    # Step 2: Create matplotlib figure and axis
    fig, ax = plt.subplots()
    ax.axis("off")
    ax.set_title("Iteration 0")

    # Step 3: Render first simulation frame
    img = ax.imshow(frames[0], cmap=cmap, interpolation="nearest")

    # Step 4: Define update function for animation
    def update(i):
        img.set_data(frames[i])
        ax.set_title(f"Iteration {i} | Wind: {winds[i]}")

        return [img]

    # Step 5: Create animation and save to file
    anim = FuncAnimation(fig, update, frames = len(frames), interval = 1000 / fps, blit=False)
    writer = PillowWriter(fps=fps)
    anim.save(output_path, writer=writer)

    # Step 6: Close figure and release resources
    plt.close(fig)
