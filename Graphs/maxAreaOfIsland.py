class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
           
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            
            return (1 + dfs(r+1,c)+
                        dfs(r-1,c)+
                        dfs(r,c+1)+
                        dfs(r,c-1))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(area,maxArea)
        return maxArea


         
            
