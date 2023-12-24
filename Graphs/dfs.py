def bfs(graph, startVertex):
    stack = [startVertex]
    visited = set()
    visited.add(startVertex)
    dfsOrder = []

    while stack:
        vertex = stack.pop()
        dfsOrder.append(vertex)

        for v in graph[vertex]:
            if v not in visited:
                visited.add(v)
                stack.append(v)

    return dfsOrder

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F', 'G'},
    'D': {'B'},
    'E': {'B', 'H'},
    'F': {'C'},
    'G': {'C'},
    'H': {'E'}
}
startVertex = "A"
print(bfs(graph, startVertex))
