# https://leetcode.com/problems/new-21-game
# Simple DP by iterating in reverse

from itertools import accumulate


def new21Game(n: int, k: int, maxPts: int) -> float:
    dp = [0] * (n + 1)
    for i in range(k, n + 1):
        dp[i] = 1

    suf = list(accumulate(dp[::-1]))[::-1] + [0]

    for i in reversed(range(k)):
        dp[i] = 1 / maxPts * (suf[i + 1] - suf[min(n + 1, i + maxPts + 1)])
        suf[i] = dp[i] + suf[i + 1]
    return dp[0]


print(new21Game(n=21, k=17, maxPts=10))

# # slightly more complicated dp solution
# # DP optimization and dimension reduction
# # Note that trivial DP is O(n^3), with dp[i][j] = probability of having a score of j after i moves
# # Apply the following 2 optimizations:
# # 1. to transition to `j`, the previous state form a contiguous segment -> use range queries
# # 2. remove dimension `i` entirely by let dp[j] = probability of having a score of j after ANY number of moves
#
# class FenwickTree:  # uses 1-indexing
#     def __init__(self, size: int):
#         self.bit = [0] * (size + 1)
#
#     def update(self, i: int, diff: float) -> None:
#         """Add diff to self.bit[i]"""
#         while i < len(self.bit):
#             self.bit[i] += diff
#             i += i & (-i)
#
#     def query(self, i: int):
#         """Get the sum up to the i-th element (inclusive)"""
#         total = 0
#         while i > 0:
#             total += self.bit[i]
#             i -= i & (-i)
#         return total
#
#     def range_sum(self, left, right):
#         if left > right:
#             return 0
#         return self.query(right) - self.query(left - 1)
#
#
# def new21Game(n: int, k: int, maxPts: int) -> float:
#     p = 1 / maxPts
#     dp = [0] * (n + 1)
#     dp[0] = 1  # before the game starts, you will always have 0 points
#     bit = FenwickTree(n + 1)
#     bit.update(1, 1)  # update first element to match dp
#
#     for i in range(1, n + 1):
#         total = bit.range_sum(max(0, i - maxPts) + 1, min(i, k))
#         dp[i] += p * total
#         bit.update(i + 1, p * total)
#
#     print(dp)
#     return bit.range_sum(k + 1, n + 1)
#
#
# print(new21Game(n=21, k=17, maxPts=10))
# print(new21Game(10, 7, 2))
