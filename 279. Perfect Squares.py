# https://leetcode.com/problems/perfect-squares/
#
# Using DP + optimizations:
# - dp[i] is how many perfect squares you need to add to i
# - use lookup table for squaring
# - using integer square root

from math import isqrt
from itertools import accumulate


def numSquares(n: int) -> int:
    # precompute squares using the prefix sum of odd numbers for O(1) squaring
    squared = [0] + list(accumulate([i for i in range(1, 1000, 2)]))

    # optional optimization: number is perfect square
    if squared[isqrt(n)] == n:
        return 1

    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # base case

    # for every number, find the minimum numbers you need to add using previously computed values
    for i in range(1, n + 1):
        for j in range(1, isqrt(i) + 1):  # j must be sqrt(i) or less, otherwise, i - j^2 < 0
            dp[i] = min(dp[i], dp[i - squared[j]] + 1)

    return dp[-1]


print(numSquares(8405))
