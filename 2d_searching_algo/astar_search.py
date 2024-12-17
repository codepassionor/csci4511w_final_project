import heapq
import random
from state_space import CityGraph
from bfs import bfs

def reconstruct_path(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return list(reversed(path))

def find_path(city_graph, start, goal):
    # find nodes
    start_node = city_graph.get_city_at(start)
    goal_node = city_graph.get_city_at(goal)

    # priority queue
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # track prev nodes
    came_from = {}
    
    # costs from start to node
    g_score = {start: 0}
    
    # heuristic
    f_score = {start: start_node.distance_to(goal_node)}
    
    # track explored nodes
    closed_set = set()

    # track visited
    visited = set()
    
    while open_set:
        # get the node with the lowest f_score
        current_f, current = heapq.heappop(open_set)

        current_node = city_graph.get_city_at(current)

        visited.add(current)
        
        if current == goal:
            path = reconstruct_path(came_from, current)
            total_cost = sum(
                city_graph.get_city_at(path[i]).distance_to(city_graph.get_city_at(path[i+1]))
                for i in range(len(path) - 1)
            )
            return (path, total_cost, len(closed_set))
        
        closed_set.add(current)
        
        for neighbor_node in current_node.get_neighbors():
            neighbor = neighbor_node.get_location()

            if neighbor in closed_set:
                continue
            
            # Calculate tentative g_score
            tentative_g_score = g_score[current] + current_node.distance_to(neighbor_node)
            
            # Check if this is a better path
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Update path
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                
                # Calculate f_score
                f_score_value = tentative_g_score + neighbor_node.distance_to(goal_node)
                
                # Add to open set
                heapq.heappush(open_set, (f_score_value, neighbor))

# demo
if __name__ == "__main__":
    city_graph = CityGraph(1000, 1000)
    city_graph.populate_graph(100)

    city_locations = city_graph.get_city_locations()

    print(city_graph.get_cities())

    [start_loc, goal_loc] = random.choices(city_locations, k=2)

    print("start:", start_loc)
    print("goal:", goal_loc)

    (path, total_cost, visited) = find_path(city_graph, start_loc, goal_loc)
    print("-------------ASTAR-------------")
    print("Path:", " -> ".join([str(x) for x in path]))
    print(f"Path length: {len(path)}")
    print(f"Total path cost: {total_cost:.2f}")
    print(f"Total locations visited: {visited}")

    (path, total_cost, visited) = bfs(city_graph, start_loc, goal_loc)
    print("-------------BFS-------------")
    print("Path:", " -> ".join([str(x) for x in path]))
    print(f"Path length: {len(path)}")
    print(f"Total path cost: {total_cost:.2f}")
    print(f"Total locations visited: {visited}")