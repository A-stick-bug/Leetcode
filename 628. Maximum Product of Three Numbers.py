from typing import List


def maximumProduct(nums: List[int]) -> int:
    nums.sort()
    res = -float('inf')
    res = max(res, nums[-1] * nums[-2] * nums[-3])
    res = max(res, nums[0] * nums[1] * nums[-1])
    return res


print(maximumProduct([-1, -2, -3]))
