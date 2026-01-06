# https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists
# Bitmask DP + submasks
# Similar idea to https://dmoj.ca/problem/dpu
# Submask iteration: https://cp-algorithms.com/algebra/all-submasks.html
#
# dp[mask] = minimum cost, set bits represents what has been merged into 1
# To transition efficiently, we precompute the size and median of subsets
#
# TC: O(3^n + 2^n * m), m=2000

def minMergeCost(lists: list[list[int]]) -> int:
    n = len(lists)
    inf = 1 << 60

    states = 1 << n
    median = [-1] * states
    size = [-1] * states
    for mask in range(1, states):
        arr = []
        for i in range(n):
            if mask & (1 << i):
                arr.extend(lists[i])
        median[mask] = sorted(arr)[(len(arr) - 1) // 2]
        size[mask] = len(arr)

    dp = [inf] * states
    for mask in range(1, states):
        if mask.bit_count() == 1:  # individual is free
            dp[mask] = 0
            continue
        submask = mask
        while submask:
            other = mask ^ submask
            dp[mask] = min(dp[mask], (dp[other]
                                      + dp[submask]
                                      + abs(median[other] - median[submask])
                                      + size[other]
                                      + size[submask]))
            submask = (submask - 1) & mask  # go to next

    return dp[-1]


print(minMergeCost(lists=[[1, 3, 5], [2, 4], [6, 7, 8]]))
print(minMergeCost(lists=[[1, 1, 5], [1, 4, 7, 8]]))
print(minMergeCost(lists=[[1], [3]]))
print(minMergeCost(lists=[[1], [1]]))
