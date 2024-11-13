
N = int(input("Enter the number of Queens: "))

def printBoard(baord):
    for i in range(N):
        for j in range(N):
            print(baord[i][j], end=" ")
        print()

def isSafe(row, col, slashCode, backslashCode,
           rowLookup, slashLookup, backslashLookup):
    if(slashLookup[slashCode[row][col]] or 
       backslashLookup[backslashCode[row][col]] or
       rowLookup[row]):
        return False
    return True

def Solve(board, col, slashCode, backslashCode,
        rowLookup, slashLookup, backslashLookup):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(i, col, slashCode, backslashCode,
                rowLookup, slashLookup, backslashLookup):
            board[i][col] = 1
            rowLookup[i] = True
            backslashLookup[backslashCode[i][col]] = True
            slashLookup[slashCode[i][col]] = True
            if Solve(board, col + 1, slashCode, backslashCode,
                    rowLookup, slashLookup, backslashLookup):
                return True
            board[i][col] = 0
            rowLookup[i] = False
            backslashLookup[backslashCode[i][col]] = False
            slashLookup[slashCode[i][col]] = False
    return False

def Solve_Queen():

    board = [[0 for i in range(N)]
            for j in range(N)]
    slashCode = [[0 for i in range(N)]
                for j in range(N)]
    backslashCode = [[0 for i in range(N)]
                for j in range(N)]
    
    rowLookup = [False] * N
    x = 2 * N -1
    slashLookup = [False] * x
    backslashLookup = [False] * x

    for rr in range(N):
        for cc in range(N):
            slashCode[rr][cc] = rr + cc
            backslashCode[rr][cc] = rr - cc + (N - 1)

    if not Solve(board, 0, slashCode, backslashCode,
                 rowLookup, slashLookup, backslashLookup):
        print("The Solution Does not Exist")
        return False
    printBoard(board)

Solve_Queen()