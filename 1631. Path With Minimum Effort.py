import heapq


def minimumEffortPath(heights) -> int:  # using dijkstra's algorithm
    inf = 10**7
    ROWS, COLS = len(heights), len(heights[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    distances = [[inf] * COLS for _ in range(ROWS)]
    distances[0][0] = 0

    pq = [(0, 0, 0)]  # (max effort, row, col)
    while pq:
        cost, row, col = heapq.heappop(pq)

        if row == ROWS - 1 and col == COLS - 1:
            return cost

        for dr, dc in directions:
            new_r = row + dr
            new_c = col + dc
            if ROWS > new_r >= 0 and COLS > new_c >= 0:
                diff = max(cost, abs(heights[new_r][new_c] - heights[row][col]))
                if diff < distances[new_r][new_c]:
                    distances[new_r][new_c] = diff
                    heapq.heappush(pq, (diff, new_r, new_c))


print(minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
