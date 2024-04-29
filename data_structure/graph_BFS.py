graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, start_vertex):
    visited = set()
    visited.add(start_vertex)
    queue = []
    queue.append(start_vertex)
    while len(queue) > 0:
        vertex = queue.pop(0)
        print(vertex)
        neighboring_vertices = graph[vertex]
        for neighboring_vertex in neighboring_vertices:
            if neighboring_vertex not in visited:
                visited.add(neighboring_vertex)
                queue.append(neighboring_vertex)


BFS(graph, "A")

def DFS(graph, start_vertex):
    visited = set()
    visited.add(start_vertex)
    stack = []
    stack.append(start_vertex)
    while len(stack) > 0:
        vertex = stack.pop()
        print(vertex)
        neighboring_vertices = graph[vertex]
        for neighboring_vertex in neighboring_vertices:
            if neighboring_vertex not in visited:
                visited.add(neighboring_vertex)
                stack.append(neighboring_vertex)


DFS(graph, "A")
