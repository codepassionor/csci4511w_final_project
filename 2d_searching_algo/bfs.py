import time
import psutil
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Record the starting time and memory usage
process = psutil.Process()
start_time = time.time()
start_mem = process.memory_info().rss  # Resident Set Size in bytes

# Perform BFS
result = bfs(graph, 'A')

# Record the ending time and memory usage
end_time = time.time()
end_mem = process.memory_info().rss

# Calculate elapsed time and memory difference
elapsed_time = end_time - start_time
memory_used = end_mem - start_mem  # in bytes, can convert to KB or MB if needed

print("BFS Result:", result)
print("Time taken: {:.6f} seconds".format(elapsed_time))
print("Memory increase: {} bytes (approximately {:.2f} KB)".format(memory_used, memory_used / 1024.0))
