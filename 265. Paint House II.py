# 2 solutions

from typing import List


def minCostII(costs: List[List[int]]) -> int:
    """
    Fast: O(NK)
    Instead of having 2 inner for loops, we only need one as all houses can just take the min cost of the previous row,
    except for the house with the same color as the min house, that house needs to take the second smallest
    """

    N, K = len(costs), len(costs[0])
    dp = costs  # copy so that the cost of the current house is already there

    for h in range(1, N):
        prev = dp[h - 1]  # previous row
        first = 0  # store indices of first and second smallest values in the previous row
        second = 1
        for c in range(1, K):
            if prev[c] <= prev[first]:
                second = first
                first = c
            elif prev[c] < prev[second]:
                second = c

        for c in range(K):
            if c == first:  # same color as min, take second min instead
                dp[h][c] += prev[second]
            else:  # otherwise, take the min
                dp[h][c] += prev[first]

    return min(dp[-1])


print(minCostII([[1, 5, 3], [2, 9, 4]]))


def minCostII_slow(costs: List[List[int]]) -> int:
    """ DP, similar to Paint House I, there are now K colors instead of 3
    Same logic as before, current house = (previous house of different color and min cost) + (cost of current house)
    Slow: O(N * K^2) """

    inf = 1 << 10
    N, K = len(costs), len(costs[0])
    dp = costs  # copy so that the cost of the current house is already there

    # for every house, we get previous with different color and lowest cost
    for i in range(1, N):
        for j in range(K):  # calculate for each color of the current house
            lowest = inf
            for color in range(K):  # check all previous houses of different color to get minimum
                if color != j:  # can't have same color
                    lowest = min(lowest, costs[i - 1][color])
            dp[i][j] += lowest

    return min(dp[-1])
