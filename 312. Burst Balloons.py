# ⭐ INTERVAL DP IS HARD
# note to self: write bottom up solution later when reviewing this
#
# https://leetcode.com/problems/burst-balloons/description/
# Interval DP, dp[i][j] has the best answer in the interval [i:j]
# N < 300, suggesting a O(n^3) solution, there are n^2 intervals so on each recursive call, we should have N operations

from functools import cache


def maxCoins(nums: list[int]) -> int:
    nums = [1] + nums + [1]  # padding to prevent index error
    n = len(nums)

    @cache
    def solve(l, r):
        if l > r:  # invalid interval
            return 0

        res = 0
        for i in range(l, r+1):
            gain = nums[l - 1] * nums[i] * nums[r + 1]
            res = max(res, gain + solve(l, i - 1) + solve(i + 1, r))
        return res

    return solve(1, n - 2)


print(maxCoins(nums=[3, 1, 5, 8]))
