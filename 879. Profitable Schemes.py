# https://leetcode.com/problems/profitable-schemes/
# Hard knapsack DP with extra dimension
#
# for each group, we can choose to do it or not do it, if we do it, we add the profit and subtract the number of people
# this is one of the few cases where we have to pass the profit as a dp state (instead of a variable)
# note: top down is easy, like all knapsack, bottom up is especially hard here

from functools import cache


def profitableSchemes_2(PPL: int, MIN_PROFIT: int, group: list[int], profit: list[int]) -> int:
    dp = [[0] * (PPL + 1) for i in range(MIN_PROFIT + 1)]
    dp[0][0] = 1  # 1 way to get 0 money with 0 people

    for gain, ppl_needed in zip(profit, group):
        for i in reversed(range(MIN_PROFIT + 1)):
            for j in reversed(range(PPL - ppl_needed + 1)):
                dp[min(i + gain, MIN_PROFIT)][j + ppl_needed] += dp[i][j]  # reach future states from current

    return sum(dp[MIN_PROFIT]) % (10 ** 9 + 7)


print(profitableSchemes_2( 5, 3, group = [2,2], profit = [2,3]))

# iterative approach 1: MLE
def profitableSchemes(n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
    @cache
    def solve(i, ppl, gain):
        if ppl < 0:
            return 0
        if i == len(group):
            return gain >= minProfit
        return solve(i + 1, ppl - group[i], gain + profit[i]) + solve(i + 1, ppl, gain)

    return solve(0, n, 0)
