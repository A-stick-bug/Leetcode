from collections import deque


def shortestDistance(grid) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (-0, -1)]
    q = deque()

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if grid[i][j] == 1:
                q.append((i, j))

    while q:
        row, col = q.popleft()
        for dr,dc in directions:
            new_r = row + dr
            new_c = col + dc
            if ROWS > new_r >= 0 and ROWS > new_c >= 0 and grid[new_r][new_c] == 0:
                q.append((new_r,new_c))
