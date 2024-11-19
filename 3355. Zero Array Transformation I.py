# https://leetcode.com/problems/zero-array-transformation-i/description/
# classic difference array problem

from itertools import accumulate


def isZeroArray(nums: list[int], queries: list[list[int]]) -> bool:
    n = len(nums)
    diff = [0] * (n + 1)
    for l, r in queries:
        diff[l] += 1
        diff[r + 1] -= 1
    dec = list(accumulate(diff))
    return all(dec[i] >= nums[i] for i in range(n))


print(isZeroArray(nums=[1, 0, 1], queries=[[0, 2]]))
print(isZeroArray(nums=[1, 3, 2, 1], queries=[[1, 3], [0, 2]]))
