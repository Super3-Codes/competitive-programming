class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = defaultdict(int)
        output = []
        def dfs(node):

            color[node] = 1
            result = True
            for neighboors in graph[node]:
                if color[neighboors] == 0:
                    result = result and dfs(neighboors)
                elif color[neighboors]== 1:
                    color[neighboors] == 3
                    return False
            if result == True:
                output.append(node)
                color[node] = 2
            return result

        for node in range(len(graph)):
            
            if color[node] == 0:
                print(node)
                result = dfs(node)
        return [i for i in range(len(graph)) if color[i] == 2]
            
