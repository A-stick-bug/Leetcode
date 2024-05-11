def satisfiesConditions(grid) -> bool:
    n, m = len(grid), len(grid[0])
    for i in range(n - 1):
        for j in range(m):
            if grid[i][j] != grid[i + 1][j]:
                return False
    for i in range(n):
        for j in range(m - 1):
            if grid[i][j] == grid[i][j + 1]:
                return False
    return True


print(satisfiesConditions(grid=[[1, 0, 2], [1, 0, 2]]))
