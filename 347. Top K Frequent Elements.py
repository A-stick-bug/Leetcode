from collections import Counter
from typing import List
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    # negative frequency for max heap
    most_frequent = [(-frequency, num) for num, frequency in count.items()]
    heapq.heapify(most_frequent)

    return [heapq.heappop(most_frequent)[1] for _ in range(k)]


# simpler solution without heap (technically most_common uses heap though)
def no_heap(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return [i[0] for i in count.most_common(k)]


print(topKFrequent([1, 1, 1, 2, 3, 4, 3, 3, 3], 3))
