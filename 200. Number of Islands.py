def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
            return
        grid[row][col] = "0"
        for r, c in directions:
            dfs(row + r, col + c)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                dfs(i, j)
                count += 1
    return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(numIslands(grid))
