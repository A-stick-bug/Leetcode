# BFS within a range and with a bunch of restrictions
# tricky part: you can't go back twice in a row, so when going backwards, do not mark the node as visited

from typing import List
from collections import deque


def minimumJumps(forbidden: List[int], a: int, b: int, x: int) -> int:
    forbidden = set(forbidden)  # faster checks for if a node is forbidden
    MAX = 2000 + a + b  # sometimes, going once beyond 2000 gives a shorter path
    vis = [False] * MAX
    vis[0] = True
    q = deque([(0, False, 0)])  # location (int), jumped back in previous move (bool), distance (int)

    while q:
        cur, prev_back, dist = q.popleft()

        if cur == x:
            return dist

        # try jumping forwards
        forward = cur + a
        if (forward < MAX) and (not vis[forward]) and (forward not in forbidden):
            vis[forward] = True
            q.append((forward, False, dist + 1))

        # try jumping backwards
        # note that we DO NOT mark the node as visited
        backwards = cur - b
        if (backwards >= 0) and (not vis[backwards]) and (backwards not in forbidden) and (not prev_back):
            vis[backwards] = True
            q.append((backwards, True, dist + 1))

    return -1


# if you pass this test case, your solution probably works
print(minimumJumps(forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], a = 29, b = 98, x = 80))
