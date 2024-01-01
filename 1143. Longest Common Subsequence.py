# using tabulation/bottom up DP
def longestCommonSubsequence_iterative(text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in reversed(range(n)):  # fill in reverse as we start with the smaller sub problems
        for j in reversed(range(m)):
            if text1[i] == text2[j]:  # equal letters, increase the longest answer by 1
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:  # either exclude a letter in the first or second work
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


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
