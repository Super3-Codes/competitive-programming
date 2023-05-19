class Solution:
    
    def dfs(self, graph, node, visit,result):
        visit.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visit:
                self.dfs(graph,neighbor,visit,result)
            
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        for account in accounts:
            for i in range(1,len(account)):
                for j in range(i+1,len(account)):
                    graph[account[i]].add(account[j])
                    graph[account[j]].add(account[i])
        
        visited = set()
        output = []
        for account in accounts:
            for emailIndex in range(1,len(account)):
                if account[emailIndex] not in visited:
                    result = []
                    self.dfs(graph,account[emailIndex],visited,result)
                    
                    output.append([account[0]]+sorted(result))
        return output
