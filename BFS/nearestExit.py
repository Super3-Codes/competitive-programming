class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS,COLS = len(maze), len(maze[0])
        visited = set()
        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        visited.add((entrance[0],entrance[1]))
        inbound = lambda newRow, newCol :  0 <= newRow < ROWS and 0 <= newCol < COLS 
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            size = len(queue)
            for i in range ((size)):
                row, col,count = queue.popleft()
                if (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1):
                    if(row,col) != (entrance[0],entrance[1]):
                        return count
                for x,y in directions:
                    newRow, newCol = row + x, col + y
                    if inbound(newRow,newCol) and (newRow,newCol) not in visited and maze[newRow][newCol] == "." :
                        queue.append((newRow,newCol,count + 1))
                        visited.add((newRow,newCol))
        return -1

       
