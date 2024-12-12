# Python program for A* Search Algorithm with Time and Memory Measurement
import math
import heapq
import time
import psutil

# Define the Cell class
class Cell:
    def __init__(self):
        # Parent cell's row index
        self.parent_i = 0
        # Parent cell's column index
        self.parent_j = 0
        # Parent cell's height index
        self.parent_k = 0
        # Total cost of the cell (f = g + h)
        self.f = float('inf')
        # Cost from start to this cell
        self.g = float('inf')
        # Heuristic cost from this cell to destination
        self.h = 0

# Define the size of the grid
ROW = 9
COL = 10
HEIGHT = 10

# Check if a cell is valid (within the grid)
def is_valid(row, col, height):
    return (0 <= row < ROW) and (0 <= col < COL) and (0 <= height < HEIGHT)

# Check if a cell is unblocked
def is_unblocked(grid, row, col, height):
    return grid[row][col][height] == 1

# Check if a cell is the destination
def is_destination(row, col, height, dest):
    return row == dest[0] and col == dest[1] and height == dest[2]

# Calculate the heuristic value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, height, dest):
    return math.sqrt((row - dest[0]) ** 2 + (col - dest[1]) ** 2 + (height - dest[2]) ** 2)

# Trace the path from source to destination
def trace_path(cell_details, dest):
    print("The Path is:")
    path = []
    row = dest[0]
    col = dest[1]
    height = dest[2]

    # Trace the path from destination to source using parent cells
    while not (cell_details[row][col][height].parent_i == row and cell_details[row][col][height].parent_j == col and cell_details[row][col][height].parent_k == height):
        path.append((row, col, height))
        temp_row = cell_details[row][col][height].parent_i
        temp_col = cell_details[row][col][height].parent_j
        temp_height = cell_details[row][col][height].parent_k
        row = temp_row
        col = temp_col
        height = temp_height

    # Add the source cell to the path
    path.append((row, col, height))
    # Reverse the path to get the path from source to destination
    path.reverse()

    # Print the path
    for i in path:
        print("->", i, end=" ")
    print()

# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1], src[2]) or not is_valid(dest[0], dest[1], dest[2]):
        print("Source or destination is invalid")
        return

    # Check if the source and destination are unblocked
    if not is_unblocked(grid, src[0], src[1], src[2]) or not is_unblocked(grid, dest[0], dest[1], dest[2]):
        print("Source or the destination is blocked")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1], src[2], dest):
        print("We are already at the destination")
        return

    # Initialize the closed list (visited cells)
    closed_list = [[[False for _ in range(HEIGHT)] for _ in range(COL)] for _ in range(ROW)]
    # Initialize the details of each cell
    cell_details = [[[Cell() for _ in range(HEIGHT)] for _ in range(COL)] for _ in range(ROW)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    k = src[2]
    cell_details[i][j][k].f = 0.0
    cell_details[i][j][k].g = 0.0
    cell_details[i][j][k].h = 0.0
    cell_details[i][j][k].parent_i = i
    cell_details[i][j][k].parent_j = j
    cell_details[i][j][k].parent_k = k

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j, k))

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        i = p[1]
        j = p[2]
        k = p[3]
        closed_list[i][j][k] = True

        # For each direction, check the successors
        directions = [
            (0, 0, 1),  # Up
            (0, 0, -1), # Down

            (0, 1, 0),    # East
            (1, 0, 0),    # South
            (0, -1, 0),   # West
            (-1, 0, 0),   # North
            (1, 1, 0),    # Southeast
            (1, -1, 0),   # Southwest
            (-1, 1, 0),   # Northeast
            (-1, -1, 0),   # Northwest

            (0, 1, 1),    # East Up
            (1, 0, 1),    # South Up
            (0, -1, 1),   # West Up 
            (-1, 0, 1),   # North Up
            (1, 1, 1),    # Southeast Up
            (1, -1, 1),   # Southwest Up
            (-1, 1, 1),   # Northeast Up
            (-1, -1, 1),   # Northwest Up

            (0, 1, -1),    # East Down
            (1, 0, -1),    # South Down
            (0, -1, -1),   # West Down
            (-1, 0, -1),   # North Down
            (1, 1, -1),    # Southeast Down
            (1, -1, -1),   # Southwest Down
            (-1, 1, -1),   # Northeast Down
            (-1, -1, -1)   # Northwest Down
        ]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            new_k = k + dir[2]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j, new_k) and is_unblocked(grid, new_i, new_j, new_k) and not closed_list[new_i][new_j][new_k]:
                # If the successor is the destination
                if is_destination(new_i, new_j, new_k, dest):
                    # Set the parent of the destination cell
                    cell_details[new_i][new_j][new_k].parent_i = i
                    cell_details[new_i][new_j][new_k].parent_j = j
                    cell_details[new_i][new_j][new_k].parent_k = k
                    print("The destination cell is found")
                    # Trace and print the path from source to destination
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell_details[i][j][k].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, new_k, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell_details[new_i][new_j][new_k].f == float('inf') or cell_details[new_i][new_j][new_k].f > f_new:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j, new_k))
                        # Update the cell details
                        cell_details[new_i][new_j][new_k].f = f_new
                        cell_details[new_i][new_j][new_k].g = g_new
                        cell_details[new_i][new_j][new_k].h = h_new
                        cell_details[new_i][new_j][new_k].parent_i = i
                        cell_details[new_i][new_j][new_k].parent_j = j
                        cell_details[new_i][new_j][new_k].parent_k = k

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

# Function to measure time and memory consumption of A* Search
def measure_a_star_performance(grid, src, dest):
    """
    Measures the time and memory consumption of the A* Search algorithm.

    Args:
        grid (list of lists): The grid representing the map (1 for unblocked, 0 for blocked).
        src (list): The source cell coordinates [row, col].
        dest (list): The destination cell coordinates [row, col].

    Returns:
        None
    """
    # Initialize the process for memory measurement
    process = psutil.Process()

    # Record the starting time and memory usage
    start_time = time.time()
    start_mem = process.memory_info().rss  # Resident Set Size in bytes

    # Perform A* Search
    a_star_search(grid, src, dest)

    # Record the ending time and memory usage
    end_time = time.time()
    end_mem = process.memory_info().rss

    # Calculate elapsed time and memory difference
    elapsed_time = end_time - start_time
    memory_used = end_mem - start_mem  # in bytes

    print("\nA* Search Performance Metrics:")
    print(f"Time taken: {elapsed_time:.6f} seconds")
    print(f"Memory increase: {memory_used} bytes (approximately {memory_used / 1024:.2f} KB)")

# Driver Code
def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    h = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1]
    ]
    grid = []
    for i in range(ROW):
        grid.append([row[:] for row in h])
    


    # Define the source and destination
    src = [8, 7, 9]
    dest = [0, 0, 0]

    # Run the A* Search algorithm and measure performance
    measure_a_star_performance(grid, src, dest)

if __name__ == "__main__":
    main()