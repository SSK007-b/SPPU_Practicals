def isSafe(board, row, col, n):
    for i in range(n):
        if board[i][col] == 'Q':
            return False
    
    for i,j in zip(range(row, -1, -1), range(col, -1,-1)):
        if board[i][j] == 'Q':
            return False
    
    for i,j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True

def solveQueens(board, row,n):
    if row == n:
        return True
    for col in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 'Q'
            if solveQueens(board, row+1, n):
                return True
            board[row][col] = '.'
    return False

if __name__ == "__main__":
    n = int(input("Enter the number Queens "))
    board = [['.' for _ in range(n)] for _ in range(n)]
    i, j = map(int, input("Enter the Position of the First Queen in (0,0) format ").split(','))
    board[i][j] = 'Q'
    if solveQueens(board, i + 1, n):
        for row in board:
            print(' '.join(row))
    else:
        print("No Solution")