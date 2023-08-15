# using prefix sum array so each query is constant time
# create it in the constructor, so it can be reused

from typing import List
from itertools import accumulate


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.psa = list(accumulate(nums))  # create a prefix sum array to achieve O(1) per query

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:  # nothing to minus if it starts from the first element
            return self.psa[right]
        else:
            return self.psa[right] - self.psa[left-1]
