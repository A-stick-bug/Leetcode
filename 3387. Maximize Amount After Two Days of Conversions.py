# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions
# Dijkstra's
# Refer to https://dmoj.ca/problem/dmpg15s6 for optimal solution
# Note: it's probably faster to invert the second graph and only run it once

from typing import List
from collections import defaultdict
from heapq import heappush, heappop


def maxAmount(initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]],
              rates2: list[float]) -> float:
    graph1 = defaultdict(list)
    for (a, b), c in zip(pairs1, rates1):
        graph1[a].append((b, c))
        graph1[b].append((a, 1 / c))

    graph2 = defaultdict(list)
    for (a, b), c in zip(pairs2, rates2):
        graph2[a].append((b, c))
        graph2[b].append((a, 1 / c))

    def search(start, val, graph):
        costs = defaultdict(int)
        costs[start] = val
        pq = [(-val, start)]  # make negative for max heap
        while pq:
            cost, node = heappop(pq)
            cost = -cost

            for adj, multi in graph[node]:
                new_cost = cost * multi
                if costs[adj] < new_cost:
                    costs[adj] = new_cost
                    heappush(pq, (-new_cost, adj))
        return costs

    day1 = search(initialCurrency, 1, graph1)
    best = 0
    for k, val in day1.items():
        best = max(best, search(k, val, graph2)[initialCurrency])

    return best


print(maxAmount(initialCurrency="EUR", pairs1=[["EUR", "USD"], ["USD", "JPY"]], rates1=[2.0, 3.0],
                pairs2=[["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]], rates2=[4.0, 5.0, 6.0]))
print(maxAmount(initialCurrency="NGN", pairs1=[["NGN", "EUR"]], rates1=[9.0], pairs2=[["NGN", "EUR"]], rates2=[6.0]))
print(maxAmount(initialCurrency="USD", pairs1=[["USD", "EUR"]], rates1=[1.0], pairs2=[["EUR", "JPY"]], rates2=[10.0]))
