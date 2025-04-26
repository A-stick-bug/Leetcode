# https://leetcode.com/problems/unit-conversion-i/description/
# Notice that the graph is actually a tree with edges going away from 0
# We can do a dfs or bfs while keeping track of the current cumulative product (mod 1e9+7)

def baseUnitConversions(conversions: list[list[int]]) -> list[int]:
    MOD = 10 ** 9 + 7
    n = len(conversions) + 1
    graph = [[] for _ in range(n)]
    for a, b, c in conversions:
        print(a, b)
        graph[a].append((b, c))

    res = [-1] * n
    res[0] = 1
    stack = [(0, 1)]
    while stack:
        cur, val = stack.pop()
        for adj, mul in graph[cur]:
            new_val = val * mul % MOD
            res[adj] = new_val
            stack.append((adj, new_val))
    return res


print(baseUnitConversions(conversions=[[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 2], [4, 6, 3], [5, 7, 4]]))
