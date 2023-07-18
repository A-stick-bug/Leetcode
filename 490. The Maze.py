from collections import deque


def hasPath(maze, start, destination):
    ROWS, COLS = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    row, col = start[0], start[1]
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

    # travel in one direction until a one is reached
    def travel(r, c, dr, dc):
        while 0 <= r < ROWS and 0 <= c < COLS and maze[r][c] != 1:
            r += dr
            c += dc
        return (r - dr, c - dc)

    q = deque()
    q.append((row, col))
    while q:
        row, col = q.popleft()
        if visited[row][col]:
            continue
        visited[row][col] = True

        if row == destination[0] and col == destination[1]:
            return True

        for dr, dc in directions:
            q.append(travel(row, col, dr, dc))

    return False


maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [1, 2]
print(hasPath(maze, start, destination))
