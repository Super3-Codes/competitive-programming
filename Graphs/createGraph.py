def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def vertex(graph, u):
    if u not in graph:
        print()
    else:
        print(' '.join(str(v) for v in graph[u]))

n = int(input())
k = int(input())

graph = {}
for _ in range(k):
    operation, *args = map(int, input().split())
    if operation == 1:
        add_edge(graph, *args)
    elif operation == 2:
        vertex(graph, *args)
