# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner
# Dijkstra's algorithm, prioritize minimizing cost, distance does not matter

from heapq import heappush, heappop


def minimumObstacles(grid: list[list[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    inf = 1 << 30
    rem = [[inf] * m for _ in range(n)]

    pq = [(grid[0][0], 0, 0)]
    while pq:
        d, r, c = heappop(pq)
        if r == n - 1 and c == m - 1:
            return d
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and d + grid[nr][nc] < rem[nr][nc]:
                rem[nr][nc] = d + grid[nr][nc]
                heappush(pq, (d + grid[nr][nc], nr, nc))


print(minimumObstacles(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]))
