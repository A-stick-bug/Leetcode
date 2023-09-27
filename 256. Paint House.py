# DP, for each house, the minimum cost = cost of the current house + previous house of different color

from typing import List


def minCost(costs: List[List[int]]) -> int:
    n = len(costs)
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = costs[0]  # base state

    for i in range(1, n):  # get minimum cost for previous house of different color
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
    return min(dp[-1])