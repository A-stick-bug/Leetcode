# https://leetcode.com/problems/sliding-puzzle
# brute force bfs
# state: current board
# TC: O(n!) where n is the number of cells

from collections import deque


def slidingPuzzle(board: list[list[int]]) -> int:
    n = 2
    m = 3

    def store(state):
        return tuple(map(tuple, state))

    def get_adj(state):
        adj_states = []
        for i in range(n):
            for j in range(m):
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ai, aj = i + di, j + dj
                    if not (0 <= ai < n and 0 <= aj < m):
                        continue
                    if state[ai][aj] == 0:
                        new_state = [row.copy() for row in state]
                        new_state[i][j], new_state[ai][aj] = new_state[ai][aj], new_state[i][j]
                        adj_states.append(new_state)
        return adj_states

    q = deque([board])
    dist = {store(board): 0}
    while q:
        cur = q.popleft()
        if cur == [[1, 2, 3], [4, 5, 0]]:
            return dist[store(cur)]
        for adj in get_adj(cur):
            if store(adj) in dist:
                continue
            dist[store(adj)] = dist[store(cur)] + 1
            q.append(adj)
    return -1


print(slidingPuzzle(board=[[1, 2, 3], [4, 0, 5]]))
