#!/usr/bin/python3


import sys


def printBoard(board):
    if any(1 in x for x in board):
        print([[idx, board[idx].index(1)] for idx, val in enumerate(board)])


def isSafe(row, square, chessboard, N, diag):
    if chessboard[row][square]:
        return False
    if square - diag >= 0 and chessboard[row][square - diag]:
        return False
    if square + diag < (N) and chessboard[row][square + diag]:
        return False
    if row == 0:
        return True
    return isSafe(row - 1, square, chessboard, N, diag + 1)


def placeSquare(row, position, chessboard, N):
    for square in range(position, N):
        if 1 in chessboard[row]:
            return 0
        if not isSafe(row - 1, square, chessboard, N, 1):
            continue
        chessboard[row][square] = 1
        return
    return 1

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

if not str.isdigit(N):
    print("N must be a number")
    sys.exit(1)

N = int(N)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = 0

while queen != N:
    chessboard = [[0 for x in range(N)] for x in range(N)]
    chessboard[0][queen] = 1
    position = 0
    row = 1
    while row < N:
        if placeSquare(row, position, chessboard, N):
            row -= 1
            position = chessboard[row].index(1)
            chessboard[row][position] = 0
            position += 1
            if not row:
                break
        else:
            row += 1
            position = 0
    printBoard(chessboard)
    queen += 1
