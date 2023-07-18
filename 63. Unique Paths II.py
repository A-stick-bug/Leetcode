def uniquePathsWithObstacles(obstacleGrid) -> int:
    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = 1

    if obstacleGrid[0][0] == 1:
        return 0

    # process first row and column separately to prevent index out of bounds
    j = 0  # first col
    for i in range(1, rows):
        if obstacleGrid[i][j] == 1:
            continue
        else:
            dp[i][j] += dp[i - 1][j]

    i = 0  # first col
    for j in range(1, cols):
        if obstacleGrid[i][j] == 1:
            continue
        else:
            dp[i][j] += dp[i][j - 1]

    for i in range(1, rows):
        for j in range(1, cols):
            if obstacleGrid[i][j] == 1:
                continue
            else:
                dp[i][j] += dp[i][j - 1] + dp[i - 1][j]

    return dp[-1][-1]
