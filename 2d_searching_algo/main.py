import random
from state_space import CityGraph
from astar import astar
from bfs import bfs
from dfs import dfs

def run_tests(x, y, connectivity, n_nodes, n_tests):
    sum_astar_locations_explored = 0
    sum_bfs_locations_explored = 0
    sum_dfs_locations_explored = 0

    sum_astar_path_costs = 0
    sum_bfs_path_costs = 0
    sum_dfs_path_costs = 0

    sum_astar_runtime = 0
    sum_bfs_runtime = 0
    sum_dfs_runtime = 0

    for _ in range(n_tests):
        city_graph = CityGraph(x, y, connectivity)
        city_graph.populate_graph(n_nodes)

        city_locations = city_graph.get_city_locations()

        [start_loc, goal_loc] = random.choices(city_locations, k=2)

        # print("start:", start_loc)
        # print("goal:", goal_loc)

        # print("-------------ASTAR-------------")
        (path, total_cost, visited, runtime) = astar(city_graph, start_loc, goal_loc)
        # print("Path:", " -> ".join([str(x) for x in path]))
        # print(f"Path length: {len(path)}")
        # print(f"Total path cost: {total_cost:.2f}")
        # print(f"Total locations visited: {visited}")
        # print(f"Total runtime in seconds: {runtime:.2f}")

        sum_astar_locations_explored += visited
        sum_astar_path_costs += total_cost
        sum_astar_runtime += runtime

        # print("-------------BFS-------------")
        (path, total_cost, visited, runtime) = bfs(city_graph, start_loc, goal_loc)
        # print("Path:", " -> ".join([str(x) for x in path]))
        # print(f"Path length: {len(path)}")
        # print(f"Total path cost: {total_cost:.2f}")
        # print(f"Total locations visited: {visited}")
        # print(f"Total runtime in seconds: {runtime:.2f}")

        sum_bfs_locations_explored += visited
        sum_bfs_path_costs += total_cost
        sum_bfs_runtime += runtime

        # print("-------------DFS-------------")
        (path, total_cost, visited, runtime) = dfs(city_graph, start_loc, goal_loc)
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
        file.write(f"AVG RUNTIME: {sum_astar_runtime / 100:.2f}\n")
        file.write("\n")
        file.write("-------------BFS STATS-------------\n")
        file.write(f"AVG # OF LOCATIONS EXPLORED: {sum_bfs_locations_explored / 100:.2f}\n")
        file.write(f"AVG PATH COST: {sum_bfs_path_costs / 100:.2f}\n")
        file.write(f"AVG RUNTIME: {sum_bfs_runtime / 100:.2f}\n")
        file.write("\n")
        file.write("-------------DFS STATS-------------\n")
        file.write(f"AVG # OF LOCATIONS EXPLORED: {sum_dfs_locations_explored / 100:.2f}\n")
        file.write(f"AVG PATH COST: {sum_dfs_path_costs / 100:.2f}\n")
        file.write(f"AVG RUNTIME: {sum_dfs_runtime / 100:.2f}\n\n")


if __name__ == "__main__":
    # with open("final_stats.txt", "a") as file:
    #     file.write("-------------2D, 100x100, 1% density (100 nodes), k=2-------------\n\n")
    # run_tests(100, 100, 2, 100, 30)

    # with open("final_stats.txt", "a") as file:
    #     file.write("-------------2D, 100x100, 10% density (1000 nodes), k=2-------------\n\n")
    # run_tests(100, 1000, 2, 100, 30)

    # with open("final_stats.txt", "a") as file:
    #     file.write("-------------2D, 100x100, 50% density (5000 nodes), k=2-------------\n\n")
    # run_tests(100, 5000, 2, 100, 30)
    pass