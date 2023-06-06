class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1]:
            return -1
        queue = deque()
        queue.append((0, 0))
        distance = 1
        
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return distance
                
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 0:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 1
            
            distance += 1
        
        return -1
