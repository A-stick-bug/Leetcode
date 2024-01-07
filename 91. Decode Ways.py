# https://leetcode.com/problems/decode-ways
# General 1D DP
# watch out for the zeros because individual zeros are invalid, it must come in the form of "10" or "20"


def numDecodings_iterative(s: str):
    """basically just reversed the recursive code below"""
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1  # base cases
    dp[n - 1] = int(s[-1] != "0")

    for i in reversed(range(n - 1)):
        double = int(s[i] + s[i + 1])  # using 2 letters
        if s[i] == "0":
            dp[i] = 0
        elif double <= 26:
            dp[i] = dp[i + 1] + dp[i + 2]
        else:
            dp[i] = dp[i + 1]
    return dp[0]


print(numDecodings_iterative("226"))

######################################
# slower recursive code, easier to understand
from functools import cache


def numDecodings(s: str) -> int:
    n = len(s)

    @cache
    def solve(i):
        """i is the current position in s"""
        if (i == n - 1 and s[i] != "0") or i == n:  # used all letters
            return 1

        if s[i] == "0":  # invalid decoding
            return 0

        double = s[i] + s[i + 1]
        if int(double) <= 26:  # there are 2 possible mappings here
            return solve(i + 1) + solve(i + 2)
        else:
            return solve(i + 1)

    return solve(0)
