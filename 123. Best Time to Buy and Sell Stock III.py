# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# buy sell stock problem with at most 2 transactions, state machine DP
# when buying a stock, we transition from the previous row of the dp table (previously bought stocks)

def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    hold = [[0] * n for _ in range(2)]
    sold = [[0] * n for _ in range(2)]

    for stock in range(2):
        hold[stock][0] = -prices[0]
        for day in range(1, n):
            sold[stock][day] = max(sold[stock][day - 1], hold[stock][day - 1] + prices[day])  # do nothing or sell
            hold[stock][day] = max(hold[stock][day - 1], sold[stock - 1][day - 1] - prices[day])  # do nothing or buy

    return sold[-1][-1]


print(maxProfit(prices=[1, 2, 3, 4, 5]))
