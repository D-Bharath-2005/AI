from collections import deque

capacities = (4, 3)
goal = 2
visited = set()
queue = deque([(0, 0)])
steps = []  # To store steps for output

while queue:
    state = queue.popleft()
    if state in visited:
        continue
    visited.add(state)
    steps.append(state)  # Track each visited state as a step
    print(f"Step {len(steps)}: {state}")  # Print the current step

    if goal in state:
        print(f"Solution found: {state}")
        break

    a, b = state
    queue.extend([
        (capacities[0], b),  # Fill jug A
        (a, capacities[1]),  # Fill jug B
        (0, b),              # Empty jug A
        (a, 0),              # Empty jug B
        (max(0, a - (capacities[1] - b)), min(capacities[1], a + b)),  # Pour A to B
        (min(capacities[0], a + b), max(0, b - (capacities[0] - a)))   # Pour B to A
    ])
