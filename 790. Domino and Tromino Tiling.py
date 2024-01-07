# https://leetcode.com/problems/domino-and-tromino-tiling
# solution looks like n^2, unsure though

from functools import cache


def numTilings(n: int) -> int:
    @cache
    def solve(i, j):
        if i > n or j > n:  # invalid tilling
            return 0
        if i == n and j == n:  # valid tilling
            return 1

        total = 0
        if i == j:
            total += solve(i + 1, j + 1)  # tile domino vertically
            total += solve(i + 2, j + 2)  # tile 2 dominos horizontally
            total += 2 * solve(i + 2, j + 1)  # tile tromino, x2 since there are 2 symmetrical orientations
        else:
            total += solve(i + 1, j + 1)   # tile 1 domino horizontally, technically is (i, j+2) but swap i and j
            total += solve(i + 1, j + 2)  # tile tromino

        return total

    return solve(0, 0) % 1_000_000_007


print(numTilings(2))
