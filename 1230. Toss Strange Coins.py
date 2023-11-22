# https://leetcode.com/problems/toss-strange-coins/
# probability DP
# 2 possibilities for each coin, there will be overlapping states
# time complexity of O(2^n) is reduced to O(N*T) using memoization

from functools import cache


def probabilityOfHeads(prob: list[float], target: int) -> float:
    @cache
    def solve(coin, heads):
        if heads > target:  # too many heads, dead end
            return 0
        if coin >= len(prob):  # out of coins, check if we have the right around of heads
            return heads == target
        # the current coin is either heads or tails
        return prob[coin] * solve(coin + 1, heads + 1) + (1 - prob[coin]) * solve(coin + 1, heads)

    return solve(0, 0)


print(probabilityOfHeads(prob=[0.5, 0.5, 0.5, 0.5, 0.5], target=0))
