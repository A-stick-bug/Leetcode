from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    res = 0

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if matrix[r][c] == "1":  # matrix and dp have 0 and 1 indexing respectively
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                res = max(res, dp[r][c])
    return res ** 2  # squared because we are looking for area
