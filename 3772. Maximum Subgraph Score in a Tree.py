# https://leetcode.com/problems/maximum-subgraph-score-in-a-tree
# Standard tree rerooting DP problem
# take answer above and below each node, then combine to get answer
#
# TC: O(n)

from typing import List


def maxSubgraphScore(n: int, edges: List[List[int]], good: List[int]) -> List[int]:
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    good = list(map(lambda x: x if x else -1, good))

    below = good.copy()  # max value of current subtree (root at 0), current node is forced
    above = [0] * n  # max value ABOVE current node (excluding current)

    # transition: below[cur] = max(0, above[prev] + good[prev] + sum(children of prev excluding current))
    # sum(children of prev excluding current) = below[prev] - good[prev] - max(0, below[cur])

    def solve(cur, prev):
        for adj in graph[cur]:
            if adj == prev:
                continue
            solve(adj, cur)
            if below[adj] > 0:
                below[cur] += below[adj]

    def reroot(cur, prev):
        if cur != 0:
            above[cur] = max(0, above[prev] + good[prev] + (below[prev] - good[prev] - max(0, below[cur])))
        for adj in graph[cur]:
            if adj == prev:
                continue
            reroot(adj, cur)

    solve(0, -1)
    reroot(0, -1)
    # print(below)
    # print(above)

    ans = [i + j for i, j in zip(above, below)]
    return ans
