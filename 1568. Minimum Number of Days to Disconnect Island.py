"""
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/

Tarjan's algorithm to find articulation points on a grid graph
Note: brute force also works

Key observations:
- we can cut off a corner of an island in 2 moves (this will be our maximum possible answer)
- however, if there is an articulation point in the graph, we can do it in one move
- special cases: there is only water: 0 moves, there is 1 island: 1 move
"""


def minDays(grid: list[list[int]]) -> int:
    N, M = len(grid), len(grid[0])
    low_link = [[-1] * M for _ in range(N)]
    node_id = [[-1] * M for _ in range(N)]
    time = 0
    found_ap = False
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(r, c, prev_r, prev_c):
        nonlocal time, found_ap
        node_id[r][c] = low_link[r][c] = time
        time += 1

        child = 0
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):  # out of bounds
                continue
            if (r == prev_r and c == prev_c) or grid[nr][nc] == 0:  # don't go back to previous cell
                continue

            if node_id[nr][nc] == -1:  # not visited
                child += 1
                dfs(nr, nc, r, c)
                low_link[r][c] = min(low_link[r][c], low_link[nr][nc])
                if low_link[nr][nc] >= node_id[r][c] and prev_r != -1:
                    found_ap = True

            else:  # back edge
                low_link[r][c] = min(low_link[r][c], node_id[nr][nc])

        if prev_r == -1 and child > 1:  # special case when root is an articulation point
            found_ap = True

    components = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                continue
            if node_id[i][j] == -1:  # only check if it hasn't been processed yet
                dfs(i, j, -1, -1)
                components += 1

    if components != 1:  # already split
        return 0
    elif found_ap or sum(sum(i) for i in grid) == 1:  # graph has articulation point OR corner case: only 1 island
        return 1
    else:
        return 2


print(minDays(grid=[[0, 1, 1, 1],
                    [0, 1, 1, 0]]))
