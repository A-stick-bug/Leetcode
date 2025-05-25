# https://leetcode.com/problems/maximum-weighted-k-edge-path
# Graph DP, optimized with bitmask
# TC: O(n * k * t)

def maxWeight(n: int, edges: list[list[int]], k: int, t: int) -> int:
    graph = [[] for _ in range(n)]
    for a, b, c in edges:
        graph[a].append((b, c))

    down = [[0] * (k + 1) for _ in range(n)]  # dp[cur][length] = bitmask of all possible weights

    mask = (1 << t) - 1  # mask containing valid bits (<=t)

    def solve(cur):
        if down[cur][0] != 0:  # cache
            return
        down[cur][0] = 1  # length 0, weight 0
        for adj, w in graph[cur]:
            solve(adj)
            for le in range(1, k + 1):
                down[cur][le] |= (down[adj][le - 1] << w)
                down[cur][le] &= mask  # clear useless bits

    for i in range(n):
        solve(i)

    best = -1
    for cur in range(n):  # loop all length k starting for each node
        if down[cur][k]:
            best = max(best, down[cur][k].bit_length() - 1)  # .bit_length() gives highest bit
    return best


print(maxWeight(
    n=3,
    edges=[[0, 1, 1], [1, 2, 2]],
    k=2,
    t=4
))
