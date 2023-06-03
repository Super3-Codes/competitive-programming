class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def dfs(node):
            result = False
            colors[node] = 1
            for neigh in adj_list[node]:
                if colors[neigh] == -1:
                    result = result or dfs(neigh,1)
                if colors[neigh] == 1:
                    return True
            colors[node] = 0
            return result
        for node in range(len(givenNodes)):
            if colors[node] == -1:
                result = dfs(node)
                if result:
                    return True
        return False

