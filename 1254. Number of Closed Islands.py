def closedIsland(grid):
    def dfs(row, col):
        # If the current cell is out of bounds or is not a 0, return
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        if grid[row][col] != 0:
            return

        # Mark the current cell as visited
        grid[row][col] = 1

        # Recursively call the DFS function on the neighboring cells
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    num_closed_islands = 0

    # Mark all the boundary cells as visited
    # by calling the DFS function on the first and last row and column
    for row in range(len(grid)):
        dfs(row, 0)
        dfs(row, len(grid[0]) - 1)

    for col in range(len(grid[0])):
        dfs(0, col)
        dfs(len(grid) - 1, col)

    # Traverse all the cells in the grid
    # and call the DFS function on each cell that is a 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == 0:
                # Call the DFS function on the current cell
                dfs(row, col)

                # If the island is closed (i.e., all neighboring cells are 1s),
                # increment the counter for the number of closed islands
                num_closed_islands += 1

    return num_closed_islands