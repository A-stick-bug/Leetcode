# https://leetcode.com/problems/reach-end-of-array-with-max-score/
#
# Let N = 50, the length and width of the board
# Let K be the number of pawns
#
# - precompute all pairs shortest path in the grid, O(N^4)
#   - OPTIMIZATION: we actually only need the paths between all pairs of pawns -> O(K * N^2)
# - use bitmask DP and some game theory to get answer, O(K * 2^K)
#   - state: [mask][location][alice's move?]
#      - note that we always end at a pawn location (K possible locations)
#   - state transitions use the precomputed shortest paths
#
# TRICK: put precomputing outside the Class, so it is only done once

from collections import deque

N = 50
inf = 1 << 60
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
dist = [[[[inf] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]


def bfs(x1, y1):
    queue = deque([(x1, y1)])
    dist[x1][y1][x1][y1] = 0
    while queue:
        x, y = queue.popleft()
        current_dist = dist[x1][y1][x][y]
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[x1][y1][nx][ny] == inf:
                dist[x1][y1][nx][ny] = current_dist + 1
                queue.append((nx, ny))


for x1 in range(N):  # all pairs shortest path
    for y1 in range(N):
        bfs(x1, y1)


def maxMoves(kx: int, ky: int, positions: list[list[int]]) -> int:
    positions.insert(0, [kx, ky])
    n = len(positions)
    cache = [[[-1] * (1 << n) for _ in range(n)] for _ in range(2)]

    def solve(state, cur, alice):
        if state == (1 << n) - 1:  # all filled
            return 0
        if cache[alice][cur][state] != -1:
            return cache[alice][cur][state]

        best = 0 if alice else inf
        f = max if alice else min
        for i in range(n):
            if state & (1 << i):
                continue
            px, py = positions[i]
            cx, cy = positions[cur]
            d = dist[px][py][cx][cy]
            best = f(best, d + solve(state | (1 << i), i, alice ^ 1))
        cache[alice][cur][state] = best
        return best

    return solve(1, 0, True)


print(maxMoves(kx=1, ky=1, positions=[[0, 0]]))
print(maxMoves(kx=0, ky=2, positions=[[1, 1], [2, 2], [3, 3]]))
print(maxMoves(kx=0, ky=0, positions=[[1, 2], [2, 4]]))
