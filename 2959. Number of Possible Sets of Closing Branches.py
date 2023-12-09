# brute force all combinations of building to shut down, including no buildings
# to check if the new set of buildings and roads is valid, we run dijkstra's algorithm from all nodes

from typing import List
from itertools import combinations
import heapq


def numberOfSets(n: int, maxDistance: int, roads: List[List[int]]) -> int:
    def bfs(start, nodes):
        q = [(0, start)]
        dist = [float('inf')] * n
        dist[start] = 0
        while q:
            d, cur = heapq.heappop(q)
            for adj, nd in graph[cur]:
                if adj not in nodes or dist[adj] <= d + nd:
                    continue
                dist[adj] = d + nd
                heapq.heappush(q, (d + nd, adj))

        m = 0
        for i, v in enumerate(dist):
            if i in nodes:
                m = max(m, v)
        return m

    graph = [[] for _ in range(n)]
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    a = list(range(n))
    all_comb = []  # possible roads to close
    all_comb.append([])
    for i in range(1, n + 1):
        all_comb.extend(list(combinations(a, i)))

    total = 0
    for rem in all_comb:
        nodes = list(range(n))
        for i in rem:
            nodes.remove(i)

        highest = 0
        for node in nodes:
            highest = max(highest, bfs(node, nodes))

        if highest <= maxDistance:
            total += 1

    return total


print(numberOfSets(n=1, maxDistance=10, roads=[]))
