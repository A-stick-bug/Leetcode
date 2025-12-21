# https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/description/
# Straightforwards tree rerooting DP
# For each group, we get the sum of distances between all pairs of nodes
# TC: O(20n)

from typing import List


def interactionCosts(n: int, edges: List[List[int]], group: List[int]) -> int:
    def solve(gr):
        below = [0] * n  # number of nodes below
        dist = [0] * n  # sum of cur to nodes below

        cost = 0
        gr_total = group.count(gr)
        root = group.index(gr)

        def dp(cur, prev):
            if group[cur] == gr:  # base case
                below[cur] += 1
            for adj in graph[cur]:
                if adj == prev:
                    continue
                dp(adj, cur)
                below[cur] += below[adj]
                dist[cur] += dist[adj] + below[adj]

        def reroot(cur, prev, a_total):
            nonlocal cost
            if group[cur] == gr:
                cost += a_total
            for adj in graph[cur]:
                if adj == prev:
                    continue
                # reroot cur->adj: farther from everything except the subtree we are going towards
                new_total = a_total + (gr_total - below[adj]) - below[adj]
                reroot(adj, cur, new_total)

        dp(root, -1)
        reroot(root, -1, dist[root])

        # print(below, dist, cost)

        return cost

    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    total = 0
    for gr in set(group):
        total += solve(gr)
    return total // 2  # overcounted due to x,y = y,x
