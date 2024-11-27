# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i
# low bounds, just run bfs again after adding each edge
# note: since this is a DAG, DP also works

from collections import deque


def shortestDistanceAfterQueries(n: int, queries: list[list[int]]) -> list[int]:
    inf = 1 << 30

    def bfs(graph, start, target):
        q = deque([start])
        dist = [inf] * n
        dist[start] = 0
        while q:
            cur = q.popleft()
            if cur == target:
                return dist[cur]
            for adj in graph[cur]:
                if dist[adj] != inf:
                    continue
                q.append(adj)
                dist[adj] = dist[cur] + 1

    graph = [[i + 1] for i in range(n)]
    res = [-1] * len(queries)
    for i, (a, b) in enumerate(queries):
        graph[a].append(b)
        res[i] = bfs(graph, 0, n - 1)
    return res


print(shortestDistanceAfterQueries(n=5, queries=[[2, 4], [0, 2], [0, 4]]))
