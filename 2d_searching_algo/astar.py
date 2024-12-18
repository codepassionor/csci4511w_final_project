import heapq
import time

def reconstruct_path(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return list(reversed(path))

def astar(graph, start, goal):
    start_time = time.time()

    # find nodes
    start_node = graph.get_city_at(start)
    goal_node = graph.get_city_at(goal)

    # priority queue
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # track prev nodes
    came_from = {}
    
    # costs from start to node
    g_scores = {start: 0}
    
    # track explored nodes
    closed_set = set()
    
    while open_set:
        # get the node with the lowest f_score
        _, current = heapq.heappop(open_set)

        if current in closed_set:
            continue

        closed_set.add(current)

        current_node = graph.get_city_at(current)

        # print(current_node, len(closed_set))

        
        if current == goal:
            path = reconstruct_path(came_from, current)
            total_cost = sum(
                graph.get_city_at(path[i]).distance_to(graph.get_city_at(path[i+1]))
                for i in range(len(path) - 1)
            )
            runtime = time.time() - start_time
            return (path, total_cost, len(closed_set), runtime)
        
        for neighbor_node in current_node.get_neighbors():
            neighbor = neighbor_node.get_location()

            if neighbor in closed_set:
                continue

            came_from[neighbor] = current

            # path from start to node
            g_score = g_scores[current] + current_node.distance_to(neighbor_node)
            g_scores[neighbor] = g_score

            # heuristic from node to goal
            h_score = neighbor_node.distance_to(goal_node)
            
            # f(x) final value
            f_score = g_score + h_score
            
            heapq.heappush(open_set, (f_score, neighbor))