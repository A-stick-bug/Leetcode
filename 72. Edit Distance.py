# https://leetcode.com/problems/edit-distance/description/
# faster iterative version

def minDistance_iterative(s: str, t: str) -> int:
    n, m = len(s), len(t)

    # dp[i][j] minimum cost to match up to s[i] and t[j]
    # extra padding to prevent index out of bounds
    dp = [[1 << 30] * (m + 1) for _ in range(n + 1)]
    dp[-1][-1] = 0
    for i in reversed(range(n)):  # iterate in reverse since we are accessing dp[i+1][j+1]
        for j in reversed(range(m)):
            if s[i] == t[j]:  # same character, no cost
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j + 1],
                                   dp[i + 1][j],
                                   dp[i][j + 1])

    return dp[0][0]


# top down recursive DP
# each state branches into 3 possibilities, the cache prevents visiting a state more than once
from functools import cache


def minDistance(word1: str, word2: str) -> int:
    word1 += "."  # add a common letter to the end of each word
    word2 += "."
    n, m = len(word1), len(word2)

    @cache
    def solve(i, j):
        """i: index in first word, j: index in second work"""
        if i == n and j == m:  # matched both words
            return 0
        if i == n or j == m:  # words did not match
            return float('inf')

        if word1[i] == word2[j]:  # same letter, doesn't cost any operations
            return solve(i + 1, j + 1)

        # if we remove a letter, we try matching the next index, i+1
        # if we insert the correct letter, that's basically the same as removing a letter in the second word, j+1
        # if we replace a character, we automatically move to the next letter in both words
        return 1 + min(solve(i + 1, j), solve(i, j + 1), solve(i + 1, j + 1))

    return solve(0, 0)
