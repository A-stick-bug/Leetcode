# https://leetcode.com/problems/longest-palindromic-subsequence/
# Interval DP: dp[i][j] has the longest palindrome inside s[i:j]
# idea: First calculate base cases (length 1 and 2) then expand from them


def longestPalindromeSubseq_iterative(s: str) -> int:
    n = len(s)
    dp = [[1] * n for _ in range(n)]  # 1 letter is always a palindrome

    # create base case
    for i in range(n - 1):  # 2 letter palindromes
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2

    for i in reversed(range(n - 1)):  # fill in reverse as we are accessing dp[i+1][j]
        for j in range(i + 2, n):  # fill normally as we are accessing dp[i][j-1]
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]  # expand palindrome
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # not palindrome so we skip a letter

    return dp[0][n - 1]


print(longestPalindromeSubseq_iterative("abc"))

# top-down solution for reference, MLE
from functools import cache


def longestPalindromeSubseq(s: str) -> int:
    n = len(s)

    @cache
    def solve(i, j):
        if i < 0 or j >= n:  # out of letters to use, remove the last 2 letters
            return -2
        if s[i] == s[j]:  # equal letters, we can expand pointers
            return solve(i - 1, j + 1) + 2

        return max(solve(i - 1, j), solve(i, j + 1))  # skip a letter, similar to LCS

    res = 1
    for i in range(n - 1):
        # try both odd and even, even palindrome start at length 2, odd starts at 1
        res = max(res, 2 + solve(i, i + 1), 1 + solve(i, i))
    return res
