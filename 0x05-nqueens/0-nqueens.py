#!/usr/bin/python3
import sys


def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in enumerate(queens):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, queens=[], solutions=[]):
    """Backtracking function to find all solutions."""
    if row == n:
        solutions.append([[r, queens[r]] for r in range(n)])
        return

    for col in range(n):
        if is_safe(queens, row, col):
            solve_nqueens(n, row + 1, queens + [col], solutions)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(n, solutions=solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
