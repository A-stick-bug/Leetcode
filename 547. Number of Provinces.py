from typing import List
from collections import deque


# use BFS to find each province and mark all nodes in the province as visited
def findCircleNum(isConnected: List[List[int]]) -> int:
    def bfs(start):
        q = deque([start])
        while q:
            node = q.popleft()
            visited[node] = True

            # 'adj' is the adjacent nodes, 'connected' is whether the adjacent is corrected to the current node
            for adj, connected in enumerate(isConnected[node]):
                if connected == 1 and not visited[adj]:
                    q.append(adj)

    n = len(isConnected)
    visited = [False for _ in range(n)]
    provinces = 0

    for node in range(n):
        if not visited[node]:
            bfs(node)  # mark all nodes in this province as visited
            provinces += 1
    return provinces


graph = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(graph))
