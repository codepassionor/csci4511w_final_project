import time
import psutil
from collections import deque

# Using a Python dictionary to act as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # Set to keep track of visited nodes of the graph.

def dfs(visited, graph, node):
    """
    Performs a Depth-First Search (DFS) on a graph.

    Args:
        visited (set): A set to keep track of visited nodes.
        graph (dict): The graph represented as an adjacency list.
        node (str): The current node to process.

    Returns:
        None
    """
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Function to measure time and memory consumption of DFS
def measure_dfs_performance(graph, start_node):
    """
    Measures the time and memory consumption of the DFS algorithm.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node (str): The node from which DFS starts.

    Returns:
        None
    """
    # Initialize the process for memory measurement
    process = psutil.Process()

    # Record the starting time and memory usage
    start_time = time.time()
    start_mem = process.memory_info().rss  # Resident Set Size in bytes

    # Perform DFS
    dfs(visited, graph, start_node)

    # Record the ending time and memory usage
    end_time = time.time()
    end_mem = process.memory_info().rss

    # Calculate elapsed time and memory difference
    elapsed_time = end_time - start_time
    memory_used = end_mem - start_mem  # in bytes

    print("\nDFS Performance Metrics:")
    print(f"Time taken: {elapsed_time:.6f} seconds")
    print(f"Memory increase: {memory_used} bytes (approximately {memory_used / 1024:.2f} KB)")

# Driver Code
if __name__ == "__main__":
    print("Following is the Depth-First Search:")
    measure_dfs_performance(graph, '5')
