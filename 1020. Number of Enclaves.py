def numEnclaves(grid):
    rows = len(grid)
    cols = len(grid[0])

    def dfs(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
            return
        grid[row][col] = 0
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols - 1)
    for i in range(cols):
        dfs(0, i)
        dfs(rows - 1, i)

    count = 0
    for r in grid:
        for cell in r:
            if cell == 1:
                count += 1
    return count


grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(numEnclaves(grid))
