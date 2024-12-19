# csci4511w_final_project

**Project Outline:**

1.  **Environments:**

- Test on 2D and 3D worlds of varying sizes, densities, and connectivity levels

- **Sizes:** total range of node locations

  - 100x100 map for 2D city graph
  - 50x50x50 map for 3D checkpoint graph

- **Densities:** calculated as `total nodes / size`
  - 1%
  - 10%
  - 50%
- **Connectivity:** calculated as `(total edges / total nodes) + 1`
  - k = 2
  - k = 10

2.  **Algorithms:**

- **Uninformed:** BFS, DFS

- **Informed:** A\* (with Euclidean straight line distance heuristic)

3.  **Metrics:**

- **Runtime:** average runtime to find a solution or determine no solution exists.

- **Number of nodes explored:** how many nodes does each algorithm have to search through before getting to the goal.

- **Path cost:** cost of getting from the start node to the goal node given the algorithm's final path

**How to replicate test results:**

- 2D tests:
  - Go to `main.py` within the `2d_searching_algo` directory, scroll to the end, and uncomment the first 3 blocks under _"RUN TESTS FOR 3 DENSITY LEVELS (1%, 10%, 50%)"_
  - To obtain the test for 10-k with a 10% density level, run the last block
> [!WARNING]
> The 50% density test (3rd block) is quite computationally intensive and may take several minutes or hours.
- 3D tests:
  - Go to `main.py` within the `3d_searching_algo` directory, scroll to the end, and uncomment the first 3 blocks under _"RUN TESTS FOR 3 DENSITY LEVELS (1%, 10%, 50%)"_
  - To obtain the test for 10-k with a 10% density level, run the last block
- You are free to change the size, density levels, connectivity levels, or number of tests as you like
  - The function is defined as `run_tests(x, y, connectivity, n_nodes, n_tests)`
