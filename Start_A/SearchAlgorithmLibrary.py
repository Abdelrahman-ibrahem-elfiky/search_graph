
heuristic= {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
}
def calculate_cost_path(path):
    inti_cost = 0
    for (node, cost) in path:
        inti_cost += cost
    last_node = path[-1][0]
    h_cost = heuristic[last_node]
    f_cost = h_cost + inti_cost
    return f_cost, last_node
def A_STAR(graph, inital_state, goal_state):
    visited = []
    queue = [[(inital_state, 0)]]
    while queue:
        queue.sort(key=calculate_cost_path)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal_state:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

