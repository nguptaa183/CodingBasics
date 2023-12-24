from collections import deque

def bfs(graph, startVertex):
    queue = deque([startVertex])
    visited = set()
    visited.add(startVertex)
    bfsOrder = []

    while queue:
        vertex = queue.popleft()
        bfsOrder.append(vertex)

        for v in graph[vertex]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

    return bfsOrder

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
