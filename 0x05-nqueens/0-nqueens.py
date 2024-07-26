#!/usr/bin/python3
'''n queens module'''

import sys


def print_usage():
    print("Usage: nqueens N")
    sys.exit(1)

def print_error(message):
    print(message)
    sys.exit(1)

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, board, row, solutions):
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
    if len(sys.argv) != 2:
        print_usage()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")

    if N < 4:
        print_error("N must be at least 4")

    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)

    for solution in solutions:
        print(solution)

