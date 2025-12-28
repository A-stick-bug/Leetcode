# https://leetcode.com/problems/minimum-cost-to-acquire-required-items
# use costBoth if it is cheaper than both items
# then consider using it if it is cheaper than individual items

def minimumCost(cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
    total = 0
    if costBoth < cost1 + cost2:
        use = min(need1, need2)
        need1 -= use
        need2 -= use
        total += use * costBoth
    return total + need1 * min(costBoth, cost1) + need2 * min(costBoth, cost2)
