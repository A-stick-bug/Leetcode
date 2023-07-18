from typing import List
import heapq


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []

    window = list(map(lambda x:-x, nums[:k]))
    heapq.heapify(window)
    res.append(-heapq.heappop(window))

    for i in range(k, len(nums)):
        heapq.heappush(window,)


