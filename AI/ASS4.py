class NQueen:

    def isSafe(self, board, row, col, n):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i,j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True
    def Solve(self, board, col, n):
        if col >= n:
            return True
        for i in range(n):
            if self.isSafe(board, i, col, n):
                board[i][col] = 1
                if self.Solve(board, col + 1, n):
                    return True
                board[i][col] = 0
        return False
    
    def Solve_Queen(self, n):
        board = [[0] * n for _ in range(n)]
        if not self.Solve(board, 0, n):
            print("No Solution Exist")
            return False
        for row in board:
            print(" ".join(map(str, row)))
        return True
    
if __name__ == "__main__":
    g = NQueen()
    n = int(input("Enter the number of Queens: "))
    g.Solve_Queen(n)
