#!/usr/bin/python3
'''n queens module'''

import sys

def print_usage():
    '''Prints the usage message and exits'''
    print("Usage: nqueens N")
    sys.exit(1)

def print_error(message):
    '''Prints an error message and exits'''
    print(message)
    sys.exit(1)

def is_valid(board, row, col):
    '''Checks if placing a queen at (row, col) is valid'''
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row, solutions):
    '''Uses backtracking to solve the N queens problem'''
    if row == N:
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1, solutions)
            board[row] = -1

if __name__ == '__main__':
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print_usage()

    # Try to convert the argument to an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")

    # Check if N is at least 4
    if N < 4:
        print_error("N must be at least 4")

    # Initialize the board and solutions list
    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)

    # Print each solution
    for solution in solutions:
        print(solution)

