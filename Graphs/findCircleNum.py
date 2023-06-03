class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(node):
            visited.add(node)

            for neighbors in range(len(isConnected[0])):
                if isConnected[node][neighbors] == 1 and neighbors not in visited:
                    dfs(neighbors)
        
        for node in range(len(isConnected)):
            if node not in visited:
                dfs(node)
                count += 1
        return count            
