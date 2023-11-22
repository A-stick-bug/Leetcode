from functools import cache


def knightProbability(n: int, k: int, row: int, column: int) -> float:
    chance = 1 / 8
    dir = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]

    @cache
    def solve(row, col, move):
        if not (0 <= row < n and 0 <= col < n):  # invalid move set because we are out of the board
            return 0
        if move == 0:  # valid move set because we did all k moves and still on the board
            return 1
        return sum(solve(row + dr, col + dc, move - 1) * chance for dr, dc in dir)

    return solve(row, column, k)


print(knightProbability(n=1, k=0, row=0, column=0))
