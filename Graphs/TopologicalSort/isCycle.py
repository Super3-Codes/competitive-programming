from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        parent = [-1] * V
    
        def dfs(node):
            visited[node] = True
        
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    parent[neighbor] = node
                    if dfs(neighbor):
                        return True
                elif parent[node] != neighbor:
                    return True
        
            return False
    
        for node in range(V):
            if not visited[node]:
                if dfs(node):
                    return 1
    
        return 0


