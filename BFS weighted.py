from collections import deque, defaultdict

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 1), ('E', 7)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

visited = set()
queue = deque(['A'])
shortest_paths = defaultdict(lambda: float('inf'))  # Track shortest paths
shortest_paths['A'] = 0  # Start node distance is 0

while queue:
    node = queue.popleft()
    if node not in visited:
        visited.add(node)
        for neighbor, weight in graph[node]:
            if shortest_paths[node] + 1 < shortest_paths[neighbor]:
                shortest_paths[neighbor] = shortest_paths[node] + 1
                queue.append(neighbor)

for node, dist in shortest_paths.items():
    print(f"Shortest path to {node}: {dist}")
