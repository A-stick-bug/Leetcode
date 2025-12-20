# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible
# Combinatorics DP
# apparently the dp table is stirling numbers of the first kind

# precompute once, use for each test case
n = 1001
MOD = 10 ** 9 + 7
dp = [[0] * (n + 2) for _ in range(n + 2)]  # dp[n][k] = used n items, k visible
dp[1][1] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i + 1][j + 1] += dp[i][j]  # insert in front: new visible
        dp[i + 1][j] += dp[i][j] * i  # insert in middle: not visible
        dp[i + 1][j + 1] %= MOD
        dp[i + 1][j] %= MOD

# for i in dp:
#     print(i)


def rearrangeSticks(n: int, k: int) -> int:
    return dp[n][k] % MOD


print(rearrangeSticks(5, 5))
print(rearrangeSticks(3, 2))
print(rearrangeSticks(n=20, k=11))
