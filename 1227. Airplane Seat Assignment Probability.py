# https://leetcode.com/problems/airplane-seat-assignment-probability/
# Probability DP


# iterative version, O(n)
def nthPersonGetsNthSeat(n: int) -> float:
    if n == 1:
        return 1
    dp = [0] * n
    dp[-1] = 0

    suffix = 0  # suffix sum of dp
    for idx in reversed(range(n - 1)):
        remaining = n - idx
        dp[idx] = 1 / remaining  # takes `1`
        # takes `nxt`, every person up to `nxt` takes their own
        dp[idx] += (1 / remaining) * suffix
        suffix += dp[idx]

    return dp[0]


print(nthPersonGetsNthSeat(1))
print(nthPersonGetsNthSeat(2))
print(nthPersonGetsNthSeat(3))
print(nthPersonGetsNthSeat(4))

# # brute force version, O(n^2)
# from functools import cache
#
#
# def nthPersonGetsNthSeat(n: int) -> float:
#     @cache
#     def solve(idx):
#         if idx == n - 1:
#             return 0
#         remaining = n - idx
#         prob = 1 / remaining  # takes `1`
#         # takes `nxt`, every person up to `nxt` takes their own
#         for nxt in range(idx + 1, n):
#             prob += 1 / remaining * solve(nxt)
#         return prob
#
#     return solve(0)
