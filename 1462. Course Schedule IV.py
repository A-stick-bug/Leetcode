"""
https://leetcode.com/problems/course-schedule-iv/description/
Fast DP solution, beats 99% (as of 2023/12/24)
DFS with DP to reuse previously calculated reachable nodes

Time complexity analysis: O(N^2 + Q)
- we run a dfs from each node, but we check if it has been visited in the past, therefore, we visit each node once
- for each node, we add all reachable nodes from its children, this can take O(n) worst case
- after precomputing reachable nodes, we can answer queries in O(1)

"""


def checkIfPrerequisite(n: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    graph = [[] for _ in range(n)]
    for a, b in prerequisites:
        graph[a].append(b)

    reach = [set() for _ in range(n)]  # reach[i][j]: starting from i, we can reach j

    def dfs(cur):
        if reach[cur]:  # check if we calculated this node before
            return
        for adj in graph[cur]:
            dfs(adj)
            for i in reach[adj]:  # add reachable nodes from children
                reach[cur].add(i)
        reach[cur].add(cur)  # mark as visited (this also makes sense because a node can always reach itself)

    for start in range(n):  # run dfs starting from all nodes
        dfs(start)

    return [end in reach[start] for start, end in queries]  # answer queries
