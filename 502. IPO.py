"""
https://leetcode.com/problems/ipo/description/
Not a traditional non-trivial greedy + heap problem, but we do use a heap to improve time complexity

We can finish K projects, our goal is to maximize profit
However, some projects require you to have x profit so far before you can start it

Strategy:
Repeat K times:
- take the highest profit project so far from our heap of available projects and do it
- update our profit and add the projects we can now do to our heap
"""

from heapq import heappush, heappop


def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    n = len(profits)
    projects = list(zip(profits, capital))  # combine as tuples
    projects.sort(key=lambda x: x[1])  # sort by profit needed so far to start it

    available = []  # list of all projects we can do so far, use negative for max heap
    cur = 0
    while cur < n and projects[cur][1] <= w:  # add projects we can start right away
        heappush(available, -projects[cur][0])
        cur += 1

    for _ in range(k):
        if not available:  # can't finish any projects, return early
            return w
        best = -heappop(available)
        w += best
        while cur < n and projects[cur][1] <= w:  # add new projects we can now start
            heappush(available, -projects[cur][0])
            cur += 1

    return w


print(findMaximizedCapital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]))
