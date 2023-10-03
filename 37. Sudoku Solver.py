"""
https://leetcode.com/problems/sudoku-solver/description/

Brute force recursion with backtracking, no optimizations
Based on backtracking template

"""

from typing import List


def solveSudoku(board: List[List[str]]) -> None:
    # floor division to split into areas of 3, multiply row by 3 to remove duplicates
    box = lambda i, j: i // 3 * 3 + j // 3
    regions = [[False] * 9 for _ in range(9)]
    rows = [[False] * 9 for _ in range(9)]
    cols = [[False] * 9 for _ in range(9)]

    # fill in already existing values
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                val = int(board[i][j]) - 1  # use 0-indexing
                rows[i][val] = True
                cols[j][val] = True
                regions[box(i, j)][val] = True

    def fill(r, c):
        """tries to fill a value into board[r][c], backtrack if we can't"""

        # found a valid configuration because we just passed the last cell and haven't backtracked yet
        if r == 8 and c == 9:
            return True

        if c == 9:  # filled column, go to next row
            c = 0
            r += 1

        # value was given to us, go to next cell
        if board[r][c] != ".":
            return fill(r, c + 1)

        # try all 9 possible values
        for num in range(9):
            # this value is valid, try placing it
            if not rows[r][num] and not cols[c][num] and not regions[box(r, c)][num]:
                board[r][c] = str(num + 1)  # switch to 1-indexing
                rows[r][num] = True
                cols[c][num] = True
                regions[box(r, c)][num] = True

                # try exploring further
                if fill(r, c + 1):
                    return True

                # didn't work, backtrack
                board[r][c] = "."
                rows[r][num] = False
                cols[c][num] = False
                regions[box(r, c)][num] = False

        return False

    fill(0, 0)


# "Hardest ever Sudoku" according to:
# https://abcnews.go.com/blogs/headlines/2012/06/can-you-solve-the-hardest-ever-sudoku
# To be fair though, it did take a bit longer than usual
board = [["8", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", "3", "6", ".", ".", ".", ".", "."],
         [".", "7", ".", ".", "9", ".", "2", ".", "."],
         [".", "5", ".", ".", ".", "7", ".", ".", "."],
         [".", ".", ".", ".", "4", "5", "7", ".", "."],
         [".", ".", ".", "1", ".", ".", ".", "3", "."],
         [".", ".", "1", ".", ".", ".", ".", "6", "8"],
         [".", ".", "8", "5", ".", ".", ".", "1", "."],
         [".", "9", ".", ".", ".", ".", "4", ".", "."]]

solveSudoku(board)
for i in board:
    print(i)
