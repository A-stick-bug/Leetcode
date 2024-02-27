"""
https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
Q: count number of strictly increasing paths in a grid (strictly increasing path -> DAG)

DP[row][col]: the number of paths starting at grid[row][col]

"""

from functools import cache


def countPaths(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    MOD = 10 ** 9 + 7

    @cache
    def solve(r, c):
        total = 1
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > grid[r][c]:
                total += solve(nr, nc)
        return total % MOD

    total = 0
    for i in range(n):
        for j in range(m):
            total += solve(i, j)
    return total


print(countPaths(grid = [[1,1],[3,4]]))
