class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def allPossibleMoves(row,col):
            if min(row,col) < 0 or row >= m or col >= n:
                return 0
                
            if row == m-1 and col == n-1:
                return 1
            if (row,col) in cache:
                return cache[(row,col)]
            
            choiceOne = allPossibleMoves(row+1,col)
            choiceTwo = allPossibleMoves(row,col+1)

            cache[(row,col)] = choiceOne + choiceTwo

            return cache[(row,col)] 

        return allPossibleMoves(0,0)
