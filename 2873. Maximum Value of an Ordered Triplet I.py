# simple brute force by trying all triplets

from typing import List


def maximumTripletValue(nums: List[int]) -> int:
    n = len(nums)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                res = max(res, nums[k] * (nums[i] - nums[j]))
    return res
