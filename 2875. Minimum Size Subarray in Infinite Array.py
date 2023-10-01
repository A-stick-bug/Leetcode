from typing import List


def minSizeSubarray(nums: List[int], target: int) -> int:
    total = sum(nums)
    fulls = target // total * len(nums)  # this is how many times the entire array is used
    target %= total

    nums *= 2  # double the array because the window may cover [end:] + [:start]
    res = float('inf')
    left = 0
    cur = 0

    # sliding window (works because there are no negative values)
    for right in range(len(nums)):
        cur += nums[right]
        while cur > target:  # if the current is greater the target, shrink the window from the left
            cur -= nums[left]
            left += 1
        if cur == target:
            res = min(res, right - left + 1)

    return res + fulls if res != float('inf') else -1


print(minSizeSubarray([1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1], 83))
