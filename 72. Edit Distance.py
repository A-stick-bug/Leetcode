# https://leetcode.com/problems/edit-distance/description/
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


print(minDistance(word1="horse", word2="ros"))
