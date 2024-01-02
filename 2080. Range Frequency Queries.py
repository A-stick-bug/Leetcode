# get frequency of element in a range using binary search

from collections import defaultdict
from bisect import bisect_left, bisect_right


class RangeFreqQuery:
    def __init__(self, arr: list[int]):
        self.pos = defaultdict(list)  # keep track of the positions of each value in sorted order
        for i, val in enumerate(arr):
            self.pos[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        low = bisect_left(self.pos[value], left)
        high = bisect_right(self.pos[value], right)

        return high - low + 1
