import functools

def minCostClimbingStairs(cost):
    @functools.cache
    def climb(i):
        if i < 2:
            return 0
        min1 = cost[i-1] + climb(i-1)
        min2 = cost[i-2] + climb(i-2)
        return min(min1, min2)

    return climb(len(cost))
