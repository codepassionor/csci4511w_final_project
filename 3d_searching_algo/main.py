import random
from state_space import CheckpointGraph
from astar import astar
from bfs import bfs
from dfs import dfs

def run_tests(x, y, z, connectivity, n_nodes, n_tests):
    sum_astar_locations_explored = 0
    sum_bfs_locations_explored = 0
    sum_dfs_locations_explored = 0

    sum_astar_path_costs = 0
    sum_bfs_path_costs = 0
    sum_dfs_path_costs = 0

    sum_astar_runtime = 0
    sum_bfs_runtime = 0
    sum_dfs_runtime = 0

    for i in range(n_tests):
        print(i)
        checkpoint_graph = CheckpointGraph(x, y, z, connectivity)
        checkpoint_graph.populate_graph(n_nodes)

        checkpoint_locations = checkpoint_graph.get_checkpoint_locations()

        [start_loc, goal_loc] = random.choices(checkpoint_locations, k=2)

        # print("start:", start_loc)
        # print("goal:", goal_loc)

        # print("-------------ASTAR-------------")
        (path, total_cost, visited, runtime) = astar(checkpoint_graph, start_loc, goal_loc)
        # print("Path:", " -> ".join([str(x) for x in path]))
        # print(f"Path length: {len(path)}")
        # print(f"Total path cost: {total_cost:.2f}")
        # print(f"Total locations visited: {visited}")
        # print(f"Total runtime in seconds: {runtime:.2f}")

        sum_astar_locations_explored += visited
        sum_astar_path_costs += total_cost
        sum_astar_runtime += runtime

        # print("-------------BFS-------------")
        try:
            (path, total_cost, visited, runtime) = bfs(checkpoint_graph, start_loc, goal_loc)
        except:
            continue
        # print("Path:", " -> ".join([str(x) for x in path]))
        # print(f"Path length: {len(path)}")
        # print(f"Total path cost: {total_cost:.2f}")
        # print(f"Total locations visited: {visited}")
        # print(f"Total runtime in seconds: {runtime:.2f}")

        sum_bfs_locations_explored += visited
        sum_bfs_path_costs += total_cost
        sum_bfs_runtime += runtime

        # print("-------------DFS-------------")
        (path, total_cost, visited, runtime) = dfs(checkpoint_graph, start_loc, goal_loc)
        # print("Path:", " -> ".join([str(x) for x in path]))
        # print(f"Path length: {len(path)}")
        # print(f"Total path cost: {total_cost:.2f}")
        # print(f"Total locations visited: {visited}")
        # print(f"Total runtime in seconds: {runtime:.2f}")

        sum_dfs_locations_explored += visited
        sum_dfs_path_costs += total_cost
        sum_dfs_runtime += runtime

    # write final stats to file
    with open("final_stats.txt", "a") as file:
        file.write("-------------ASTAR STATS-------------\n")
        file.write(f"AVG # OF LOCATIONS EXPLORED: {sum_astar_locations_explored / 100:.2f}\n")
        file.write(f"AVG PATH COST: {sum_astar_path_costs / 100:.2f}\n")
        file.write(f"AVG RUNTIME: {sum_astar_runtime / 100}\n")
        file.write("\n")
        file.write("-------------BFS STATS-------------\n")
        file.write(f"AVG # OF LOCATIONS EXPLORED: {sum_bfs_locations_explored / 100:.2f}\n")
        file.write(f"AVG PATH COST: {sum_bfs_path_costs / 100:.2f}\n")
        file.write(f"AVG RUNTIME: {sum_bfs_runtime / 100}\n")
        file.write("\n")
        file.write("-------------DFS STATS-------------\n")
        file.write(f"AVG # OF LOCATIONS EXPLORED: {sum_dfs_locations_explored / 100:.2f}\n")
        file.write(f"AVG PATH COST: {sum_dfs_path_costs / 100:.2f}\n")
        file.write(f"AVG RUNTIME: {sum_dfs_runtime / 100}\n\n")


if __name__ == "__main__":
    # RUN TESTS FOR 3 DENSITY LEVELS (1%, 10%, 50%)
    # with open("final_stats.txt", "a") as file:
    #     file.write("-------------3D, 50x50x50, 1% density (1250 nodes), k=2-------------\n\n")
    # run_tests(50, 50, 50, 2, 1250, 30)

    # with open("final_stats.txt", "a") as file:
    #     file.write("-------------3D, 50x50x50, 10% density (12500 nodes), k=2-------------\n\n")
    # run_tests(50, 50, 50, 2, 12500, 30)

    # with open("final_stats.txt", "a") as file:
    #     file.write("-------------3D, 50x50x50, 50% density (62500 nodes), k=2-------------\n\n")
    # run_tests(50, 50, 50, 2, 62500, 30)

    # RUN TEST FOR 10-k CONNECTIVITY ON 10%
    with open("final_stats.txt", "a") as file:
        file.write("-------------3D, 50x50x50, 10% density (12500 nodes), k=10-------------\n\n")
    run_tests(50, 50, 50, 10, 12500, 30)
    pass