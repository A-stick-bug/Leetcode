from typing import List
from functools import cache


# looking for combinations (eg. 1,2,1 and 1,1,2 are the same thing)
def change(amount: int, coins: List[int]) -> int:
    @cache
    def solve(n, i):
        if n == 0:  # reached 0, add one to total
            return 1
        if n < 0 or i == len(coins):  # can't go below 0 or already tried all coins
            return 0

        return solve(n - coins[i], i) + solve(n, i + 1)  # either use the current coin or don't

    return solve(amount, 0)


def bottom_up_method(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in reversed(range(len(coins))):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]

    return dp[amount]


print(change(amount=5, coins=[1, 2, 5]))
