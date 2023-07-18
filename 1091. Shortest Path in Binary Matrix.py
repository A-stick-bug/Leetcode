from collections import deque


def shortestPathBinaryMatrix(grid):
    ROWS, COLS = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]

    if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
        return -1

    q = deque()
    q.append((0, 0))
    grid[0][0] = 1

    while q:
        row, col = q.popleft()
        if row == ROWS - 1 and col == COLS - 1:
            return grid[row][col]

        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc
            if ROWS > new_r >= 0 and COLS > new_c >= 0 and grid[new_r][new_c] == 0:
                grid[new_r][new_c] = grid[row][col]+1
                q.append((new_r, new_c))
    return -1


print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
