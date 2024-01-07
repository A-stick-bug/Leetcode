# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Good DP question to practice state transitions
# Similar to house robber/fibonacci problem since there is a 1 day cooldown

def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    hold = [0] * n
    sold = [0] * n

    # base cases
    hold[0] = -prices[0]  # to hold on to a stack, it costs money

    for i in range(1, n):
        sold[i] = max(sold[i - 1], hold[i - 1] + prices[i])  # either wait or sell the previous stock
        hold[i] = max(hold[i - 1], sold[i - 2] - prices[i])  # either wait or buy another stock after cooldown

    # print(hold)
    # print(sold)
    return max(sold)


print(maxProfit(prices=[6, 1, 6, 4, 3, 0, 2]))  # 7
