# https://leetcode.com/problems/critical-connections-in-a-network/
# similar to https://dmoj.ca/problem/vmss7wc16c6p3
#
# find bridges in a graph
# using tarjan's algorithm

def criticalConnections(n: int, connections: list[list[int]]) -> list[list[int]]:
    graph = [[] for _ in range(n)]
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    bridges = []
    low_link = [-1] * n  # lowest node id reachable from node i
    node_id = [-1] * n
    time = 0

    def dfs(cur, p):
        nonlocal time
        node_id[cur] = low_link[cur] = time
        time += 1

        for adj in graph[cur]:
            if adj == p:
                continue
            if node_id[adj] == -1:  # not yet visited
                dfs(adj, cur)
                low_link[cur] = min(low_link[cur], low_link[adj])
                if low_link[adj] > node_id[cur]:
                    bridges.append([cur, adj])

            else:  # back edge
                low_link[cur] = min(low_link[cur], node_id[adj])

    dfs(0, -1)
    return bridges


print(criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
