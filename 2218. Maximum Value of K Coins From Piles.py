# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles
# 2D DP, with cumulative sums

from itertools import accumulate
from functools import cache


def maxValueOfCoins(piles: list[list[int]], k: int) -> int:
    n = len(piles)
    piles = list(map(lambda x: list(accumulate([0] + x)), piles))  # PSA: taking j things from pile[i] gives pile[i][j]

    @cache
    def solve(c, i):  # we are currently on pile i, we can take c more coins
        if c == 0 or i == n:  # out of coins to take or out of piles
            return 0
        best = 0
        for take in range(min(len(piles[i]), c + 1)):  # try taking all possible amounts of coins from this pile
            best = max(best, piles[i][take] + solve(c - take, i + 1))
        return best

    return solve(k, 0)


print(maxValueOfCoins(piles=[[1, 100, 3], [7, 8, 9]], k=2))
