"""
https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
Q: Find longest strictly increasing path in a matrix

Basically the matrix can be thought of as a DAG

"""

from functools import cache


def maxIncreasingCells(mat: list[list[int]]) -> int:
    n, m = len(mat), len(mat[0])

    @cache
    def solve(r, c, cur):
        longest = 1  # longest path starting here

        # same row
        for i in range(n):
            if mat[i][c] > cur:
                longest = max(longest, 1 + solve(i, c, mat[i][c]))
        for j in range(m):
            if mat[r][j] > cur:
                longest = max(longest, 1 + solve(r, j, mat[r][j]))
        return longest

    best = 0
    for i in range(n):
        for j in range(m):
            best = max(best, solve(i, j, mat[i][j]))
    return best


print(maxIncreasingCells(mat =  [[3,1,6],[-9,5,7]]))
