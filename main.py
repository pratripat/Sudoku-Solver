import sys

#Start sudoku board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

#Returns if the particular number for that spot in the board is valid or not
def is_valid(board, i, j, n):
    row = board[i]
    col = [row[j] for row in board]
    group = [board[y+i//3*3][x+j//3*3] for y in range(3) for x in range(3)]

    return n not in row + col + group

#Recursively solves the puzzle
def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                #Try all numbers from 1-9
                for n in range(1, 10):
                    if is_valid(board, i, j, n):
                        board[i][j] = n
                        solve(board)
                        board[i][j] = 0

                return

    #Solution to the puzzle is found
    print('===========================')
    for row in board:
        print(row)
    print('===========================')

solve(board)
