from collections import deque


def canVisitAllRooms(rooms):
    graph = {}  # start = 0
    visited = {0}
    for i in range(len(rooms)):
        graph[i] = rooms[i]

    queue = deque()
    queue += graph[0]
    while queue and len(visited) < len(rooms):
        current = queue.popleft()
        if current not in visited:
            queue += graph[current]
            visited.add(current)

    return len(rooms) == len(visited)

print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))