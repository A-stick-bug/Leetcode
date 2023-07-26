# O(n), sliding window

def maxProfit(prices) -> int:
    start = end = 0
    res = 0
    while end < len(prices):
        if prices[end] >= prices[start]:  # continue moving pointer to see if it gives greater profit
            res = max(res, prices[end] - prices[start])
            end += 1

        else:  # more profit may be earned by buying at end
            start = end

    return res


print(maxProfit([7,6,4,3,1]))
