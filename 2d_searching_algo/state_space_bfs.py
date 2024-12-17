import state_space
import random
from collections import deque


def bfs(graph, start, end):
    visited = {}
    queue = deque([(start, [start])])
    while queue:
        current_loc, path = queue.popleft()
        if current_loc not in visited:
            current_node = graph.get_city_at(current_loc)
            visited[current_loc] = path
            for neighbor in current_node.get_neighbors():
                neighbor_loc = neighbor.get_location()
                if neighbor_loc not in visited:
                    if neighbor_loc == end:
                        total_cost = sum(
                            graph.cities[path[i]].distance_to(graph.cities[path[i+1]])
                            for i in range(len(path) - 1)
                        )
                        return path, total_cost, len(visited)
                    else:
                        new_path = path + [neighbor_loc]
                        queue.append((neighbor_loc, new_path))
    return None

# Example graph
city_graph = state_space.CityGraph(1000, 1000)
city_graph.populate_graph(100)
city_locations = city_graph.get_city_locations()
[start, end] = random.choices(city_locations, k=2)

visited_cities = bfs(city_graph, start, end)

path, total_cost, visited_locations = visited_cities
        
print("path:", " -> ".join([str(x) for x in path]))
print(f"\nPath length: {len(path)}")
print(f"Total path cost: {total_cost:.2f}")
print(f"Total locations visited: {visited_locations}")