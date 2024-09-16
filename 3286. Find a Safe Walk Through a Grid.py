from heapq import heappush, heappop


def findSafeWalk(grid: list[list[int]], health: int) -> bool:
    n = len(grid)
    m = len(grid[0])
    pq = [(grid[0][0], 0, 0)]
    dist = [[1 << 30] * m for _ in range(n)]
    while pq:
        dmg, r, c = heappop(pq)
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            n_dmg = dmg + grid[nr][nc]
            if n_dmg < dist[nr][nc]:
                dist[nr][nc] = n_dmg
                heappush(pq, (n_dmg, nr, nc))

    return dist[-1][-1] < health


print(findSafeWalk(grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], health=1))
print(findSafeWalk(grid=[[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], health=3))
print(findSafeWalk(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], health=5))
