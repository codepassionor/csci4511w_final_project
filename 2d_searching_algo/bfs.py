from collections import deque
import time

def bfs(graph, start, end):
    start_time = time.time()
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
                        path = path + [neighbor_loc]
                        total_cost = sum(
                            graph.get_city_at(path[i]).distance_to(graph.get_city_at(path[i+1]))
                            for i in range(len(path) - 1)
                        )
                        runtime = time.time() - start_time
                        return (path, total_cost, len(visited), runtime)
                    else:
                        new_path = path + [neighbor_loc]
                        queue.append((neighbor_loc, new_path))