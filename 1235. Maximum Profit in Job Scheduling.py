# 10-12p
# similar to https://dmoj.ca/problem/aac1p6 but no need for fenwick tree

from heapq import heappop, heappush


def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    items = list(zip(startTime, endTime, profit))
    items.sort()
    best = 0
    pending = []

    for start, end, gain in items:
        while pending and pending[0][0] <= start:  # while the current one doesn't overlap with previous
            best = max(best, pending[0][1])
            heappop(pending)

        heappush(pending, (end, best + gain))

    for _, profit in pending:  # get remaining elements
        best = max(best, profit)

    return best


print(jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
