# DP: find number of ways to get from target to 0, dp[i] = number of ways to get to 0 from i
# Problem name is misleading, it should be permutations
# Similar to [518 - Coin Change II], except in this problem we are looking for permutations, not combinations

from typing import List
from functools import cache


def combinationSum4(nums: List[int], target: int) -> int:
    """Top-down method using memoization"""

    @cache
    def solve(n):
        if n == 0:  # reached 0, add one to total
            return 1
        if n < 0:  # can't go below 0 or already tried all coins
            return 0

        res = 0
        for i in range(len(nums)):  # try all possible
            res += solve(n - nums[i])
        return res

    return solve(target)


def bottom_up(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)

    # note how the order of the 2 for loops are swapped compared to Coin Change II
    # dp[i] = number of ways to get to i
    for i in range(1, target + 1):
        for num in nums:
            if i - num < 0:  # can't go below 0
                continue
            elif i - num == 0:  # can get to 0 directly from this number
                dp[i] += 1
            else:  # can get to a smaller number that may be able to get to 0, so we add its value
                dp[i] += dp[i - num]

    return dp[-1]


print(bottom_up(nums=[1, 2, 3], target=4))
