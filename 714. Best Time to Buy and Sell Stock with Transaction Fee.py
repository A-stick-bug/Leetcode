# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# State machine DP

def maxProfit(prices: list[int], fee: int) -> int:
    n = len(prices)
    hold = [0] * n
    sold = [0] * n
    hold[0] = -prices[0]  # base case

    for i in range(1, n):
        sold[i] = max(sold[i - 1], hold[i - 1] + prices[i] - fee)  # either wait or sell the previous held stock
        hold[i] = max(hold[i - 1], sold[i - 1] - prices[i])  # either wait or buy another stock

    return sold[-1]


print(maxProfit(prices=[1, 3, 2, 8, 4, 9], fee=2))
