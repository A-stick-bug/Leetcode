# https://leetcode.com/problems/coin-change/
# dynamic programming solution
def coinChange_DP(coins, amount: int) -> int:
    dp = [0] * (amount + 1)  # base case is 0 since we can just not have any coin

    for i in range(1, amount + 1):
        res = float('inf')
        for c in coins:
            if i - c >= 0:  # reachable from a previous state, +1 since we are using an extra coin
                res = min(res, dp[i - c] + 1)
        dp[i] = res  # choose the previous state that uses the least coins

    return dp[amount] if dp[amount] != float('inf') else -1


print(coinChange_DP(coins=[1, 2, 5], amount=11))

# BFS solution
from collections import deque


def coinChange(coins, amount: int) -> int:
    q = deque()
    q.append((amount, 0))
    visited = {amount}

    while q:
        amt, n_coins = q.popleft()
        if amt == 0:
            return n_coins
        for coin in coins:
            if amt - coin >= 0 and amt - coin not in visited:
                visited.add(amt - coin)
                q.append((amt - coin, n_coins + 1))

    return -1
