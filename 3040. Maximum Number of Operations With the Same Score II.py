# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/
# using top down DP: 3 choices
# dp[val][i][j]: we can only remove if the 2 numbers add up to val, currently at i on the left and j on the right
# O(n^2)

from collections import defaultdict


def maxOperations(nums: list[int]) -> int:
    n = len(nums)
    cache = defaultdict(lambda: [[-1] * n for _ in range(n)])

    def solve(i, j, val):
        if i >= j:  # don't have enough stuff to remove
            return 0
        if cache[val][i][j] != -1:
            return cache[val][i][j]

        ans = 0
        if nums[i] + nums[i + 1] == val:
            ans = max(ans, 1 + solve(i + 2, j, val))  # remove from left
        if nums[j] + nums[j - 1] == val:
            ans = max(ans, 1 + solve(i, j - 2, val))  # remove from right
        if nums[i] + nums[j] == val:
            ans = max(ans, 1 + solve(i + 1, j - 1, val))  # remove one from both side

        cache[val][i][j] = ans
        return ans

    return max(solve(0, n - 1, nums[0] + nums[1]),
               solve(0, n - 1, nums[0] + nums[-1]),
               solve(0, n - 1, nums[-1] + nums[-2]))


print(maxOperations(nums=[3, 2, 6, 1, 4]))
