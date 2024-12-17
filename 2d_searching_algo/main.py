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

    for _ in range(100):
        city_graph = CityGraph(1000, 1000, 2)
        city_graph.populate_graph(10000)

        city_locations = city_graph.get_city_locations()

        [start_loc, goal_loc] = random.choices(city_locations, k=2)

        print("start:", start_loc)
        print("goal:", goal_loc)

        print("-------------ASTAR-------------")
        (path, total_cost, visited) = astar(city_graph, start_loc, goal_loc)
        print("Path:", " -> ".join([str(x) for x in path]))
        print(f"Path length: {len(path)}")
        print(f"Total path cost: {total_cost:.2f}")
        print(f"Total locations visited: {visited}")

        sum_astar_locations_explored += visited
        sum_astar_path_costs += total_cost

        print("-------------BFS-------------")
        (path, total_cost, visited) = bfs(city_graph, start_loc, goal_loc)
        print("Path:", " -> ".join([str(x) for x in path]))
        print(f"Path length: {len(path)}")
        print(f"Total path cost: {total_cost:.2f}")
        print(f"Total locations visited: {visited}")

        sum_bfs_locations_explored += visited
        sum_bfs_path_costs += total_cost

        print("-------------DFS-------------")
        (path, total_cost, visited) = dfs(city_graph, start_loc, goal_loc)
        print("Path:", " -> ".join([str(x) for x in path]))
        print(f"Path length: {len(path)}")
        print(f"Total path cost: {total_cost:.2f}")
        print(f"Total locations visited: {visited}")

        sum_dfs_locations_explored += visited
        sum_dfs_path_costs += total_cost

    print()
    print("-------------ASTAR STATS-------------")
    print(f"AVG # OF LOCATIONS EXPLORED: {sum_astar_locations_explored / 100}")
    print(f"AVG PATH COST: {sum_astar_path_costs / 100:.2f}")
    print()
    print("-------------BFS STATS-------------")
    print(f"AVG # OF LOCATIONS EXPLORED: {sum_bfs_locations_explored / 100}")
    print(f"AVG PATH COST: {sum_bfs_path_costs / 100:.2f}")
    print()
    print("-------------DFS STATS-------------")
    print(f"AVG # OF LOCATIONS EXPLORED: {sum_dfs_locations_explored / 100}")
    print(f"AVG PATH COST: {sum_dfs_path_costs / 100:.2f}")