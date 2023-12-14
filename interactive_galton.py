# Importing libraries 
import random

# Define a function that simulates the fall of pearls through the pegs
def simulate_fall(levels, pegs):
    # Start at the middle of the pegs
    position = (pegs - 1) // 2  
    for _ in range(levels):
        step = random.choice([-1, 1])  # -1 for left, 1 for right
        position += step
        position = max(0, min(position, pegs - 1))  # Keep within bounds
    return position

# Define a function that visualizes the state of the board
def visualize_board(levels, pegs, bins):
    red_color = "\033[91m"
    green_color = "\033[92m"
    reset_color = "\033[0m"

    # Visualize the pegs with red color
    for level in range(levels):
        offset = ' ' if level % 2 == 0 else '   '
        line = offset + '   '.join(f'{red_color}|{reset_color}' for _ in range(pegs - (level % 2)))
        print(line)
        
    # Visualize the bins with green beads
    max_bin_height = max(bins)
    for height in range(max_bin_height, 0, -1):
        line = '   '.join(f'{green_color}o{reset_color}' if bin_count >= height else ' ' for bin_count in bins)
        print(' ' + line)

    # Print the bin dividers at the bottom with red color
    bin_line = '   '.join(f'{red_color}|{reset_color}' for _ in range(pegs + 1))
    print(' ' + bin_line)

# Define a function to run the simulation
def run_simulation(levels, pegs, beads):
    # Initialize bins for the number of pegs + 1, because beads fall between pegs
    bins = [0] * (pegs + 1)
    
    # Simulate beads falling
    for _ in range(beads):
        final_position = simulate_fall(levels, pegs)
        bins[final_position] += 1
    
    visualize_board(levels, pegs, bins)

# Example usage
run_simulation(levels=20, pegs=20, beads=150)

# To be continued... (divide into two-step process: start/reset, density as background to the beads, ...)
