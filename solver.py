# solver.py

# This program aims to solve a Sudoku puzzle using the concept of recursion, backtracking and looping.
# By completing this project, I hope to further cement my understanding of Python and how to apply it to different
# contexts. I hope to incorporate a GUI and/or a way to scan a sudoku "image" and have this code act on that puzzle to
# solve it.

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


def solve(boa):
    empty = find_empty(boa)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1,10):
        if valid(boa, i, (row, col)):
            boa[row][col] = i

            if solve(boa):
                return True

            boa[row][col] = 0

    return False


def valid(boa, num, ind):
    # Check row
    for i in range(len(boa[0])):
        if boa[ind[0]][i] == num and ind[1] != i:
            return False

    # Check column
    for i in range(len(boa)):
        if boa[i][ind[1]] == num and ind[0] != i:
            return False

    # Check 3x3 box region to follow Sudoku rules
    x_box = ind[1] // 3
    y_box = ind[0] // 3

    for i in range(y_box*3, y_box*3 + 3):
        for j in range(x_box*3, x_box*3 + 3):
            if boa[i][j] == num and (i,j) != ind:
                return False

    return True


def print_board(boa):
    for i in range(len(boa)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(boa)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(boa[i][j])
            else:
                print(str(boa[i][j]) + " ", end="")


def find_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j] == 0:
                return (i, j)    # row, col

    return None


print_board(board)
solve(board)
print("______________")
print_board(board)