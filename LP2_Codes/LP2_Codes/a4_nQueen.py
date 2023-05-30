def is_safe(board, row, col):
    for i in range(col): # Check row and column
        if board[row][i] == 1:
            return False

    i, j = row, col      # Check upper diagonal
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col      # Check lower diagonal
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens(board, col):
    if col >= len(board):    # Base case: All queens are placed
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1                        # Place the queen

            if solve_n_queens(board, col + 1):       # Recursively solve for the next column
                return True

            board[i][col] = 0                        # Backtrack: Remove the queen
    return False

def print_board(board):
    for row in board:
        print(" ".join(map(str,row)))
    print()

n = int(input("Enter the board size: "))
board = [[0] * n for i in range(n)]  #Create an empty board

if solve_n_queens(board, 0):
    print("Solution found:")
    print_board(board)
else:
    print("No solution found.")