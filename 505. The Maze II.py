import heapq


def shortestDistance(maze, start, destination):
    """
    --dijkstra's--
    no need to use a dict to keep track of distances because we only want to find the distance to one node/cell
    use of heap guarantees that when a node is reached, the cost will already be the shortest
    """
    ROWS, COLS = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # travel in a direction until it hits a border (for readability, could also put this inside of the loop for queue)
    def travel(row, col, dr, dc):
        dist = 0
        while ROWS > row >= 0 and COLS > col >= 0 and maze[row][col] == 0:
            row += dr
            col += dc
            dist += 1
        return row - dr, col - dc, dist - 1

    pq = [(0, tuple(start))]

    # an alternative is to use a 'distance' dict that has inf on all values and instead of checking for already visited,
    # check of the current method of getting to the cell is shorter
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

    while pq:
        cost, node = heapq.heappop(pq)
        row, col = node

        if node == tuple(destination):
            return cost
        visited[row][col] = True

        for dr, dc in directions:
            new_r, new_c, new_cost = travel(row, col, dr, dc)

            # prevent visiting a cell more than one
            if not visited[new_r][new_c]:
                total = cost + new_cost
                heapq.heappush(pq, (total, (new_r, new_c)))
    return -1


maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(shortestDistance(maze, start, destination))
