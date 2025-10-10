# https://leetcode.com/problems/number-of-stable-subsequences/description/
# Standard subsequence DP
# 3 possible transitions at each index, like any sequence dp
# - 1. extend previous subsequence
# - 2. keep previous subsequence (ignore current)
# - 3. start new subsequence with current element
#
# We care about the previous 2 elements to determine what the next one can be
# Note: we can easily replace the dict by compressing the 6 possible states
#
# TC: O(n), with a large constant factor

from collections import defaultdict


def countStableSubsequences(nums: List[int]) -> int:
    n = len(nums)
    arr = [i % 2 for i in nums]
    dp = [defaultdict(int) for _ in range(n)]
    mod = 10 ** 9 + 7

    dp[0][(arr[0],)] = 1  # base case
    for i in range(1, n):
        for prev in dp[i - 1]:
            seq = prev + (arr[i],)
            if len(seq) == 3 and (sum(seq) in [0, 3]):  # invalid
                continue
            new_val = seq[-2:]
            dp[i][new_val] += dp[i - 1][prev]
            dp[i][new_val] %= mod

        dp[i][(arr[i],)] = 1  # new sequence

        for prev in dp[i - 1]:
            dp[i][prev] += dp[i - 1][prev]  # don't take

    return sum(dp[-1].values()) % mod
