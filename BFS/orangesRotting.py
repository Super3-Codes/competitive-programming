from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0  # To keep track of the number of fresh oranges
        minutes_passed = 0  # To track the time

        # Find all initially rotten oranges and count the number of fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Special case: If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0

        # Perform BFS to rot neighboring oranges
        while queue:
            # Process oranges level by level
            level_size = len(queue)
            for _ in range(level_size):
                row, col = queue.popleft()

                # Check all neighboring cells
                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                    queue.append((row - 1, col))
                    fresh_count -= 1
                if row + 1 < ROWS and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                    queue.append((row + 1, col))
                    fresh_count -= 1
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))
                    fresh_count -= 1
                if col + 1 < COLS and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))
                    fresh_count -= 1

            # Increment the minutes after processing each level
            minutes_passed += 1

        # If there are any fresh oranges left, it's impossible to rot all oranges
        if fresh_count > 0:
            return -1
        else:
            # Subtract 1 from minutes_passed since the last level was processed without adding any fresh oranges
            return minutes_passed - 1
