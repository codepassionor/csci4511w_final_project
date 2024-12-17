def dfs(graph, start, end):
    start_node = graph.get_city_at(start)
    end_node = graph.get_city_at(end)
    
    visited = set()
    
    stack = [(start_node, [start], 0)]
    
    while stack:
        current_node, current_path, current_cost = stack.pop()
        current_loc = current_node.get_location()
        
        visited.add(current_loc)

        if current_node == end_node:
            return (current_path, current_cost, len(visited))

        for neighbor in current_node.get_neighbors():
            neighbor_location = neighbor.get_location()
            
            if neighbor_location in visited:
                continue
            
            new_path = current_path + [neighbor_location]
            new_cost = current_cost + current_node.distance_to(neighbor)
            
            stack.append((neighbor, new_path, new_cost))