class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node == len(graph) - 1:
                return [[node]]
            result = []
            for neighbor in graph[node]:
                paths = dfs(neighbor)
                for path in paths:
                    result.append([node] + path)
            return result
        
        return dfs(0)
