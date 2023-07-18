from collections import deque


def minKnightMoves(x: int, y: int) -> int:
    # BFS solution with pruning
    directions = [(1, 2), (2, 1), (-1, 2), (1, -2), (-2, 1), (2, -1)]
    q = deque()
    q.append((0, 0, 0))
    visited = set()
    x,y = abs(x), abs(y)
    while q:
        cost, row, col = q.popleft()

        if row == x and col == y:
            return cost

        if (row, col) in visited:
            continue
        visited.add((row, col))

        for dx, dy in directions:
            q.append((cost + 1, row + dx, col + dy))


print(minKnightMoves(x=0, y=-300))
