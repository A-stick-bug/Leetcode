from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    if sum(nums) < target:  # cannot reach a sum of target
        return 0

    left = cur = 0
    res = len(nums)  # minimum window length so far
    for right in range(len(nums)):
        cur += nums[right]  # extend window forwards
        while cur - nums[left] >= target:  # try to shrink window
            cur -= nums[left]
            left += 1  # update current sum shrink

        if cur >= target:  # current window's sum is greater than the target
            res = min(res, right - left + 1)

    return res


print(minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
