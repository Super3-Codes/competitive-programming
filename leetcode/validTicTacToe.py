 def validTicTacToe(self, board: List[str]) -> bool:
        xCount = 0
        oCount = 0
        for i in range (len(board)):
            row = board[i]
            for j in range(len(row)):
                if(row[j] == 'X'):
                    xCount += 1
                elif(row[j] == 'O'):
                    oCount += 1
        if(oCount > xCount or xCount - oCount > 1):
            return False
        def winner(board,symbool):
            colmun = []
            diagonals = []
            posDiagonal  = []
            negDiagonal = []
            for i in range(3):
                col = []
                for j in range(3):
                    col.append(board[j][i])
                    if(j+i == 2):
                        posDiagonal.append(board[i][j])
                    if(i == j):
                        negDiagonal.append(board[i][j])
                colmun.append("".join(col))
            diagonals.append("".join(posDiagonal))
            diagonals.append("".join(negDiagonal))
            if (symbool == 'O'):
                
                if(board[0] == 'OOO' or board[1] == 'OOO' or board[2] == 'OOO'):
                    return True
                if(colmun[0] == 'OOO' or colmun[1] == 'OOO' or colmun[2] == 'OOO'):
                    return True
                if(diagonals[0] == 'OOO' or diagonals[1] == 'OOO'):
                    return True
            else:
                if(board[0] == 'XXX' or board[1] == 'XXX' or board[2] == 'XXX'):
                    return True
                if(colmun[0] == 'XXX' or colmun[1] == 'XXX' or colmun[2] == 'XXX'):
                    return True
                if(diagonals[0] == 'XXX' or diagonals[1] == 'XXX'):
                    return True
            return False

        if(winner(board,"X") and xCount == oCount):
            return False
        if(winner(board,"O") and xCount > oCount):
            return False
        return True
