# https://leetcode.com/problems/distinct-subsequences/
# similar to LCS, average string DP question

def numDistinct_iterative(s: str, t: str) -> int:
    N, M = len(s), len(t)
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # create base cases
    for i in range(N + 1):  # when M is at max, we successfully created string t
        dp[i][-1] = 1

    for i in reversed(range(N)):
        for j in reversed(range(M)):
            if s[i] == t[j]:  # check recursive code to understand this part
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]

    return dp[0][0]


print(numDistinct_iterative(s="abab", t="ab"))

# recursive solution with memoization (very slow, just here for reference)
from functools import cache


def numDistinct(s: str, t: str) -> int:
    n, m = len(s), len(t)

    @cache
    def solve(i, j):
        """i: index in s, j: index in t"""
        if j == m:  # created word t
            return 1
        if i == n:  # ran out of letters
            return 0

        if s[i] == t[j]:  # matched a letter in t
            return solve(i + 1, j + 1) + solve(i + 1, j)
        return solve(i + 1, j)  # didn't match, must go to next letter

    return solve(0, 0)
