# BFS solution dp could use used as well

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


print(coinChange(coins=[1,5], amount=11))
