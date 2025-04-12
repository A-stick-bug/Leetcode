# https://leetcode.com/problems/longest-cycle-in-a-graph/
# find the longest cycle in a functional graph (highly optimized solution)
# iterative 'dfs' solution


def longestCycle(edges: list[int]) -> int:
    n = len(edges)
    in_path = [False] * n
    vis = [False] * n

    def dfs(start):
        nonlocal ans

        cur = start
        path = []
        while True:
            if in_path[cur]:  # cycle found
                ans = max(ans, len(path) - path.index(cur))
                break
            elif vis[cur] or edges[cur] == -1:  # nowhere to go
                break
            else:  # go to next node
                in_path[cur] = True
                path.append(cur)
                vis[cur] = True
                cur = edges[cur]

        for node in path:  # clear current dfs path
            in_path[node] = False

    ans = 0
    for i in range(n):
        if not vis[i]:
            dfs(i)
    return ans if ans != 0 else -1


print(longestCycle(edges=[3, 3, 4, 2, 3]))
print(longestCycle(edges=[2, -1, 3, 1]))
