# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# buy sell stock problem with at most K transactions, state machine DP
# when buying a stock, we transition from the previous row of the dp table (previously bought stocks)

def maxProfit(k: int, prices: list[int]) -> int:
    n = len(prices)
    hold = [[0] * n for _ in range(k)]
    sold = [[0] * n for _ in range(k + 1)]  # extra row for padding, sold[-1][x] always returns 0 (useful when k=1)

    for stock in range(k):
        hold[stock][0] = -prices[0]
        for day in range(1, n):
            sold[stock][day] = max(sold[stock][day - 1], hold[stock][day - 1] + prices[day])  # do nothing or sell
            hold[stock][day] = max(hold[stock][day - 1], sold[stock - 1][day - 1] - prices[day])  # do nothing or buy

    return sold[k-1][-1]


print(maxProfit(k=1, prices=[6, 1, 6, 4, 3, 0, 2]))
