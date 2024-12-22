# standard grid DP
# states: [row][col][xor value]

def countPathsWithXorValue(grid: list[list[int]], k: int) -> int:
    MOD = 10 ** 9 + 7
    n = len(grid)
    m = len(grid[0])

    dp = [[[0] * 16 for _ in range(m)] for _ in range(n)]
    dp[0][0][grid[0][0]] = 1

    for i in range(n):
        for j in range(m):
            for x in range(16):
                if i > 0:
                    dp[i][j][x] += dp[i - 1][j][x ^ grid[i][j]]
                if j > 0:
                    dp[i][j][x] += dp[i][j - 1][x ^ grid[i][j]]
                dp[i][j][x] %= MOD

    return dp[n - 1][m - 1][k]


print(countPathsWithXorValue(grid=[[2, 1, 5], [7, 10, 0], [12, 6, 4]], k=11))
print(countPathsWithXorValue(grid=[[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k=2))
print(countPathsWithXorValue(grid=[[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k=10))
