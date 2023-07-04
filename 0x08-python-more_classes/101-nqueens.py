#!/usr/bin/python3
"""Solves the N-queens puzzle"""
import sys


def mos_board_initialization(z):
    """Initialize a chessboard"""
    a = []
    [a.append([]) for x in range(z)]
    [board_row.append(' ') for x in range(z) for board_row in a]
    return (a)


def copy_chess_board(a):
    """Return a copy of a chessboard."""
    if isinstance(a, list):
        return list(map(copy_chess_board, a))
    return (a)


def win_plane(a):
    """Return the list of lists representation of a solved chessboard."""
    s = []
    for x in range(len(a)):
        for y in range(len(a)):
            if a[x][y] == "Q":
                s.append([x, y])
                break
    return (s)


def chess_spot(a, row, col):
    """chess spots on a chessboard."""
    # chess spots all forward spots
    for y in range(col + 1, len(a)):
        a[row][y] = "x"
    # chess spots all backwards spots
    for y in range(col - 1, -1, -1):
        a[row][y] = "x"
    # chess spots all spots below
    for x in range(row + 1, len(a)):
        a[x][col] = "x"
    # chess spots all spots above
    for x in range(row - 1, -1, -1):
        a[x][col] = "x"
    # chess spots all spots diagonally down to the right
    y = col + 1
    for x in range(row + 1, len(a)):
        if y >= len(a):
            break
        a[x][y] = "x"
        y += 1
    # chess spots all spots diagonally up to the left
    y = col - 1
    for x in range(row - 1, -1, -1):
        if y < 0:
            break
        a[x][y]
        y -= 1
    # chess spots all spots diagonally up to the right
    y = col + 1
    for x in range(row - 1, -1, -1):
        if y >= len(a):
            break
        a[x][y] = "x"
        y += 1
    # chess spots all spots diagonally down to the left
    y = col - 1
    for x in range(row + 1, len(a)):
        if y < 0:
            break
        a[x][y] = "x"
        y -= 1


def iteration_ans(a, row, z, ans):
    """Recursively solve an N-queens puzzle."""
    if z == len(a):
        ans.append(win_plane(a))
        return (ans)

    for c in range(len(a)):
        if a[row][c] == " ":
            aa = copy_chess_board(a)
            aa[row][c] = "Q"
            chess_spot(aa, row, c)
            ans = iteration_ans(aa, row + 1, z + 1, ans)

    return (ans)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    a = mos_board_initialization(int(sys.argv[1]))
    ans = iteration_ans(a, 0, 0, [])
    for n in ans:
        print(n)
