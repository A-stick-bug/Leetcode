def minPathSum(grid) -> int:
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            # special case: top corner
            if i == 0 and j ==0:
                continue

            # top row
            elif i == 0:
                grid[i][j] += grid[i][j-1]

            # left-most column
            elif j == 0:
                grid[i][j] += grid[i-1][j]

            else:
                # take whichever is cheaper
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]
