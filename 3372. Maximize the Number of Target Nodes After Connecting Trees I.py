# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
# brute force with DFS

def maxTargetNodes(edges1, edges2, k):
    def get_within_reach(graph, start, lim):
        n = len(graph)
        stack = [start]
        vis = [-1] * n
        vis[start] = 0
        while stack:
            cur = stack.pop()
            if vis[cur] > lim:
                continue
            for adj in graph[cur]:
                if vis[adj] != -1:
                    continue
                stack.append(adj)
                vis[adj] = vis[cur] + 1
        return sum(i != -1 and i <= lim for i in vis)

    n = len(edges1) + 1
    graph1 = [[] for _ in range(n)]
    for a, b in edges1:
        graph1[a].append(b)
        graph1[b].append(a)
    m = len(edges2) + 1
    graph2 = [[] for _ in range(m)]
    for a, b in edges2:
        graph2[a].append(b)
        graph2[b].append(a)

    reach = [get_within_reach(graph2, i, k - 1) for i in range(m)]
    best = max(reach)

    res = []
    for i in range(n):
        res.append(best + get_within_reach(graph1, i, k))
    return res


print(maxTargetNodes(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                     edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], k=2))
print(maxTargetNodes(edges1=[[0, 1], [0, 2], [0, 3], [0, 4]], edges2=[[0, 1], [1, 2], [2, 3]], k=1))
