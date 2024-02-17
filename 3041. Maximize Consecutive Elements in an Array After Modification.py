"""
https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification

Sequence DP, longest consecutive sequence, you're allowed to increase any number by 1
dp: stores best answer for sequences ending at i
dp_inc: stores best answer for sequences ending at i if you got to i by increasing i-1

Note: we need to use a defaultdict instead of creating an array with 1 million elements because
runtimes on Leetcode is the total runtime across all cases, NOT the worst case of a single test case.
This question has many small cases so using defaultdict will be much faster despite the constant factor.
"""

from collections import defaultdict


def maxSelectedElements(nums: list[int]) -> int:
    nums.sort()
    dp = defaultdict(int)
    dp_inc = defaultdict(int)

    for val in nums:
        dp_inc[val + 1] = max(dp[val], dp_inc[val]) + 1
        dp[val] = max(dp[val - 1], dp_inc[val - 1]) + 1

    return max(max(dp.values()), max(dp_inc.values()))
