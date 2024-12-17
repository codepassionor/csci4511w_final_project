import state_space
import math
import random
from collections import deque


def bfs(graph, start, end):
    start_node = graph.cities[start]
    visited = []
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in node.get_neighbors():
                if neighbor not in visited:
                    neighbor_loc = (neighbor.x, neighbor.y)
                    if neighbor_loc == end:
                        return visited
                    else:
                        queue.append(neighbor)
    return None

# Example graph
city_graph = state_space.CityGraph(1000, 1000)
city_graph.populate_graph(100)
cities = city_graph.city_locations
[start, end] = random.choices(cities, k=2)

visited_cities = bfs(city_graph, start, end)
print(len(visited_cities))