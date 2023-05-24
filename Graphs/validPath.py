class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]

        # Create the adjacency list representation of the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        visited = set()

        def dfs(curr):
            if curr == destination:
                return True

            visited.add(curr)

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)
