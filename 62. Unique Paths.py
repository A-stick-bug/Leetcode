def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dp[1][1] = 1
    for r in range(1, m+1):
        for c in range(1, n+1):
            dp[r][c] += dp[r-1][c] + dp[r][c-1]
    return dp[-1][-1]


print(uniquePaths(1,2))
