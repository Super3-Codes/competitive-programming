class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        clickRow, clickCol = click[0], click[1]
        if board[clickRow][clickCol] == "M":
            board[clickRow][clickCol] = "X"
            return board
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def countMines(row, col):
            count = 0
            for r, c in directions:
                if 0 <= row+r < len(board) and 0 <= col+c < len(board[0]) and board[row+r][col+c] == 'M':
                    count += 1
            return count

        def dfs(row, col):
            if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != 'E':
                return

            mines = countMines(row, col)
            if mines > 0:
                board[row][col] = str(mines)
            else:
                board[row][col] = 'B'
                for r, c in directions:
                    dfs(row+r, col+c)

        dfs(click[0], click[1])
        return board