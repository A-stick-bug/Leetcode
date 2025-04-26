# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag
# Bitmask DP, with bit optimizations
# Due to large constraints we must only use the current bitmask as our state
# We will also be using the mask to check in degrees
#
# TC: O(2^N * N)

def maxProfit(n: int, edges: list[list[int]], score: list[int]) -> int:
    graph = [[] for _ in range(n)]
    req = [0] * n
    for a, b in edges:
        graph[a].append(b)
        req[b] |= 1 << a  # add to requirement

    dp = [-1] * (1 << n)

    def solve(mask):
        if dp[mask] != -1:
            return dp[mask]

        idx = mask.bit_count() + 1

        best = 0
        for i in range(n):
            if mask & (1 << i) or req[i] | mask != mask:  # already visited or not all requirements satisfied
                continue
            best = max(best, solve(mask | (1 << i)) + idx * score[i])

        dp[mask] = best
        return dp[mask]

    return solve(0)


print(maxProfit(n=2, edges=[[0, 1]], score=[2, 3]))
print(maxProfit(n=3, edges=[[0, 1], [0, 2]], score=[1, 6, 3]))
