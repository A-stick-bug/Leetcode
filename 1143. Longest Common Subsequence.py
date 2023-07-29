from functools import cache


# using memoization
def longestCommonSubsequence(text1: str, text2: str) -> int:
    @cache
    def solve(i1, i2):
        if i1 == len(text1) or i2 == len(text2):
            return 0

        if text1[i1] == text2[i2]:
            return solve(i1 + 1, i2 + 1) + 1

        return max(solve(i1, i2 + 1), solve(i1 + 1, i2))

    return solve(0, 0)
