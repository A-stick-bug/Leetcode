# https://leetcode.com/problems/paint-house-iv
# Dynamic programming
# - Start with the center houses and expand outwards
# - Note that since we are doing 2 houses at a time, there is another dimension in the dp table
# - The inner for loops aren't necessary, and you can just write out the transition statements
#   but this method is easier to understand

def minCost(n: int, cost: list[list[int]]) -> int:
    hf = n // 2
    inf = 1 << 60

    cost1 = cost[hf:]
    cost2 = cost[:hf][::-1]

    prev = [[inf] * 3 for _ in range(3)]

    # base case: center 2 houses
    for c1 in range(3):
        for c2 in range(3):
            if c1 == c2:
                continue
            prev[c1][c2] = cost1[0][c1] + cost2[0][c2]

    for i in range(1, hf):
        dp = [[inf] * 3 for _ in range(3)]
        for c1 in range(3):
            for c2 in range(3):
                if c1 == c2:
                    continue
                for prev1 in range(3):
                    if prev1 == c1:
                        continue
                    for prev2 in range(3):
                        if prev2 == c2 or prev2 == prev1:
                            continue
                        dp[c1][c2] = min(dp[c1][c2], prev[prev1][prev2] + cost1[i][c1] + cost2[i][c2])
        prev = dp
    return min(min(row) for row in prev)


print(minCost(n=4, cost=[[3, 5, 7], [6, 2, 9], [4, 8, 1], [7, 3, 5]]))
print(minCost(n=6, cost=[[2, 4, 6], [5, 3, 8], [7, 1, 9], [4, 6, 2], [3, 5, 7], [8, 2, 4]]))
