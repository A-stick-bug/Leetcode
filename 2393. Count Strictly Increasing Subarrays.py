"""
https://leetcode.com/problems/count-strictly-increasing-subarrays/description/

Split the array into strictly increasing parts
- If a subarray is strictly increasing, all of its sub-sub-arrays are strictly increasing too
- Array of length n has n*(n+1)//2 subarrays

"""

from typing import List


def countSubarrays(nums: List[int]) -> int:
    nums.append(0)  # make sure we count the increasing subarray at the end
    cur = 1  # length of current increasing subarray
    total = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur += 1
        else:  # current subarray is no longer strictly increasing, clear count and add to total
            total += cur * (cur + 1) // 2
            cur = 1

    return total


print(countSubarrays([1,3,5,4,4,6]))
