# https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains
# Heap solution, think in reverse
# Visualize the problem as building a binary tree on top of an array
# always extend branches from the 2 lowest nodes to minimize the maximum height

from heapq import heappush, heappop, heapify


def minEliminationTime(timeReq: list[int], splitTime: int) -> int:
    pq = timeReq.copy()
    heapify(pq)

    while len(pq) >= 2:
        top1 = heappop(pq)
        top2 = heappop(pq)
        heappush(pq, max(top1, top2) + splitTime)

    return pq[0]


print(minEliminationTime(timeReq=[10, 4, 5], splitTime=2))
