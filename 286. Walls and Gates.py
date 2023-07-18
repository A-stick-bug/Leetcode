from collections import deque


def wallsAndGates(rooms):
    # Do not return anything, modify rooms in-place instead.
    ROWS, COLS = len(rooms), len(rooms[0])
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

    q = deque()
    for i in range(ROWS):
        for j in range(COLS):
            if rooms[i][j] == 0:
                q.append((i, j))

    while q:
        row, col = q.popleft()

        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc
            if ROWS > new_r >= 0 and COLS > new_c >= 0 and rooms[new_r][new_c] == 2147483647:
                q.append((new_r, new_c))
                rooms[new_r][new_c] = min(rooms[new_r][new_c], rooms[row][col] + 1)
    return rooms


print(wallsAndGates(
    [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1],
     [0, -1, 2147483647, 2147483647]]))
