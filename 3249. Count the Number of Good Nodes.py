# https://leetcode.com/problems/count-the-number-of-good-nodes
# simple tree DP

def countGoodNodes(edges: list[list[int]]) -> int:
    N = len(edges) + 1
    graph = [[] for _ in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    total = 0

    def solve(cur, prev):
        nonlocal total
        if len(graph[cur]) == 1 and cur != 0:
            total += 1
            return 1
        childs = []
        for adj in graph[cur]:
            if adj == prev:
                continue
            childs.append(solve(adj, cur))
        if len(set(childs)) == 1:
            total += 1
        return sum(childs) + 1

    solve(0, -1)
    return total


print(countGoodNodes(
    edges=[[0, 1], [1, 2], [1, 3], [1, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10], [9, 12], [10, 11]]))
