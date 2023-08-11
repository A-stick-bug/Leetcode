# Dijkstra's algorithm
# the goal is to find a path to the end with a minimum 'max tile number'

from typing import List
import heapq


def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    vis = [[False] * n for _ in range(n)]
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pq = [(grid[0][0], 0, 0)]   # if the starting point is > 0, we have to wait

    while pq:
        time, row, col = heapq.heappop(pq)
        if row == n - 1 and col == n - 1:
            return time

        for dr, dc in dir:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < n and 0 <= new_c < n and not vis[new_r][new_c]:  # not visited yet and not out of bounds
                vis[new_r][new_c] = True
                new_time = max(time, grid[new_r][new_c])  # check if the current tile is greater than previous max
                heapq.heappush(pq, (new_time, new_r, new_c))


print(swimInWater(grid=[[0, 2], [1, 3]]))
