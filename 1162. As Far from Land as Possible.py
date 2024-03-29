from collections import deque


def maxDistance(grid) -> int:
    q = deque()
    ROWS, COLS = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for i, val in enumerate(grid):
        for j, cell in enumerate(val):
            if grid[i][j] == 1:
                q.append((i, j, 0))

    if not q or len(q) == ROWS * COLS:  # all land or all water
        return -1

    while q:
        row, col = q.popleft()
        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc
            if ROWS > new_r >= 0 and COLS > new_c >= 0 and grid[new_r][new_c] == 0:
                q.append((new_r, new_c))
                grid[new_r][new_c] = grid[row][col] + 1

    res = 0
    for i in range(ROWS):
        res = max(res,max(grid[i]))
    return res - 1
