# https://leetcode.com/problems/minimum-cost-for-tickets/
# general 1D DP, reach current state from previous states, take the min

def mincostTickets(days: list[int], costs: list[int]) -> int:
    MN = 400  # max days possible with padding
    travel = [False] * MN  # keep track of travel days
    for i in days:
        travel[i - 1] = True

    dp = [0] * MN
    for i in reversed(range(365)):
        if not travel[i]:  # don't travel this day, use the previous calculated value
            dp[i] = dp[i + 1]
        else:
            dp[i] = min(dp[i + 1] + costs[0],  # take the cheapest
                        dp[i + 7] + costs[1],
                        dp[i + 30] + costs[2])

    return dp[0]


print(mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
