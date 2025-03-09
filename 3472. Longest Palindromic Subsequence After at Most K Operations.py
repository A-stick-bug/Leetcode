# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations
# Interval DP with extra dimension
# Longest palindromic subsequence after K operations

from collections import defaultdict


def longestPalindromicSubsequence(s: str, K: int) -> int:
    if len(s) == 1:
        return 1

    s = list(map(lambda x: ord(x) - ord("a"), s))
    n = len(s)

    # base cases, 1 and 2 letters
    dp = [[defaultdict(int) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i][0] = 1
    for i in range(n - 1):
        diff = abs(s[i] - s[i + 1])
        dp[i][i + 1][0] = 2 if s[i] == s[i + 1] else 1
        if min(diff, 26 - diff) <= K:
            dp[i][i + 1][min(diff, 26 - diff)] = 2

    for i in reversed(range(n - 1)):
        for j in range(i + 2, n):
            diff = abs(s[i] - s[j])
            for k in dp[i + 1][j - 1]:
                new_cost = k + min(diff, 26 - diff)
                if new_cost <= K:
                    dp[i][j][new_cost] = max(dp[i][j][new_cost], 2 + dp[i + 1][j - 1][k])

            for k in dp[i + 1][j]:
                dp[i][j][k] = max(dp[i][j][k], dp[i + 1][j][k])
            for k in dp[i][j - 1]:
                dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k])
            for k in dp[i + 1][j - 1]:
                dp[i][j][k] = max(dp[i][j][k], dp[i + 1][j - 1][k])

    res = 1
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                res = max(res, max(dp[i][j].values()))
    return res


print(longestPalindromicSubsequence("wehzr", 3))
print(longestPalindromicSubsequence("gd", 1))
print(longestPalindromicSubsequence(s="abced", K=2))
print(longestPalindromicSubsequence(s="aaazzz", K=4))
