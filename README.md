# csci4511w_final_project

**Project Outline:**

1.  **Environments:**

- Test on 2D and 3D worlds of varying sizes, densities, and connectivity levels

-  **Sizes:** total range of node locations
	- 100x100 map for 2D city graph
	- 50x50x50 map for 3D checkpoint graph

-  **Densities:** calculated as `total nodes / size`
	- 1%
	- 10%
	- 50%
- **Connectivity:** calculated as `(total edges / total nodes) - 1`
	- k = 2
	- k = 10

2.  **Algorithms:**

-  **Uninformed:** BFS, DFS

-  **Informed:** A* (with Euclidean straight line distance heuristic)

  

3.  **Metrics:**

-  **Runtime:** average runtime to find a solution or determine no solution exists.

-  **Number of nodes explored:**  how many nodes does each algorithm have to search through before getting to the goal.

-  **Path cost:** cost of getting from the start node to the goal node given the algorithm's final path
