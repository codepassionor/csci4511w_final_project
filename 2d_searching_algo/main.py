import random
from state_space import CityGraph
from astar import astar
from bfs import bfs
from dfs import dfs

if __name__ == "__main__":
    sum_astar_locations_explored = 0
    sum_bfs_locations_explored = 0
    sum_dfs_locations_explored = 0

    sum_astar_path_costs = 0
    sum_bfs_path_costs = 0
    sum_dfs_path_costs = 0

    sum_astar_runtime = 0
    sum_bfs_runtime = 0
    sum_dfs_runtime = 0

    for _ in range(100):
        city_graph = CityGraph(100, 100, 2)
        city_graph.populate_graph(100)

        city_locations = city_graph.get_city_locations()

        [start_loc, goal_loc] = random.choices(city_locations, k=2)

        print("start:", start_loc)
        print("goal:", goal_loc)

        print("-------------ASTAR-------------")
        (path, total_cost, visited, runtime) = astar(city_graph, start_loc, goal_loc)
        print("Path:", " -> ".join([str(x) for x in path]))
        print(f"Path length: {len(path)}")
        print(f"Total path cost: {total_cost:.2f}")
        print(f"Total locations visited: {visited}")
        print(f"Total runtime in seconds: {runtime:.2f}")

        sum_astar_locations_explored += visited
        sum_astar_path_costs += total_cost
        sum_astar_runtime += runtime

        print("-------------BFS-------------")
        (path, total_cost, visited, runtime) = bfs(city_graph, start_loc, goal_loc)
        print("Path:", " -> ".join([str(x) for x in path]))
        print(f"Path length: {len(path)}")
        print(f"Total path cost: {total_cost:.2f}")
        print(f"Total locations visited: {visited}")
        print(f"Total runtime in seconds: {runtime:.2f}")

        sum_bfs_locations_explored += visited
        sum_bfs_path_costs += total_cost
        sum_bfs_runtime += runtime

        print("-------------DFS-------------")
        (path, total_cost, visited, runtime) = dfs(city_graph, start_loc, goal_loc)
        print("Path:", " -> ".join([str(x) for x in path]))
        print(f"Path length: {len(path)}")
        print(f"Total path cost: {total_cost:.2f}")
        print(f"Total locations visited: {visited}")
        print(f"Total runtime in seconds: {runtime:.2f}")

        sum_dfs_locations_explored += visited
        sum_dfs_path_costs += total_cost
        sum_dfs_runtime += runtime

    print()
    print("-------------ASTAR STATS-------------")
    print(f"AVG # OF LOCATIONS EXPLORED: {sum_astar_locations_explored / 100}")
    print(f"AVG PATH COST: {sum_astar_path_costs / 100:.2f}")
    print(f"AVG RUNTIME: {sum_astar_runtime / 100:.2f}")
    print()
    print("-------------BFS STATS-------------")
    print(f"AVG # OF LOCATIONS EXPLORED: {sum_bfs_locations_explored / 100}")
    print(f"AVG PATH COST: {sum_bfs_path_costs / 100:.2f}")
    print(f"AVG RUNTIME: {sum_bfs_runtime / 100:.2f}")
    print()
    print("-------------DFS STATS-------------")
    print(f"AVG # OF LOCATIONS EXPLORED: {sum_dfs_locations_explored / 100}")
    print(f"AVG PATH COST: {sum_dfs_path_costs / 100:.2f}")
    print(f"AVG RUNTIME: {sum_dfs_runtime / 100:.2f}")