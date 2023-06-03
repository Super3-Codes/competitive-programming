class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        colors = defaultdict(lambda: -1)
        for x , y in dislikes:
            adj_list[x].append(y)
            adj_list[y].append(x)
        def dfs(node,color):
            colors[node] = color
            result = True
            for neig in adj_list[node]:
                if  colors[neig] == -1:
                    nextColor = 1 - color 
                    result = result and dfs(neig,nextColor)
                elif  colors[neig] == color:
                    return False
            return result

        for i in range(1,len(dislikes)+1):
            if colors[i] == -1:
                result = dfs(i,0)
                if not result:
                    return False
        return True 


        
