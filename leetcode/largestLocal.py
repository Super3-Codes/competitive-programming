class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # declare a var called I
        #keep track of i until it is equal to the len of grid
        #at the same iterate over the values on the row row + 1 and row + 2
        n = len(grid) - 2
        result = [[] for _ in range(n)]
        for row in range(len(grid)-2):
            for col in range(len(grid)-2):
                values = -inf
                for i in range(row, row+3):
                    for j in range(col , col+3):
                        values = max(values,grid[i][j])
                result[row].append(values)
        return result
