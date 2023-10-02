"""
Problem: https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/description/
Credits: https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/solutions/4112091/java-c-python-stack-solution-no-dfs-no-topo/
"""

from collections import OrderedDict


def countVisitedNodes(edges):
    n = len(edges)
    res = [0] * n

    for i in range(n):
        prev = OrderedDict()
        cur = i

        # traverse until we get a cycle or reach a previously computed node
        while (cur not in prev) and (res[cur] == 0):
            prev[cur] = len(prev)
            cur = edges[cur]

        # we reached a cycle, all nodes in the cycle should have the length of the cycle as the value
        if cur in prev:
            k = len(prev) - prev[cur]  # length of cycle
            for _ in range(k):
                res[prev.popitem()[0]] = k

        # update using precalculated values in reverse order
        while prev:
            cur = prev.popitem()[0]
            res[cur] = res[edges[cur]] + 1

    return res
