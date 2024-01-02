# alternate solution using LCS: if 2 letters are the same, go to next index
# otherwise, there is a cost, and we can move one of the indices forward

def minimumDeleteSum_iterative(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    s1 = list(map(lambda x: ord(x), list(s1)))  # convert strings to ascii value list
    s2 = list(map(lambda x: ord(x), list(s2)))

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + s1[i]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    result = sum(s1 + s2) - dp[n][m] * 2  # total ascii minus the cost of the LCS
    return result


print(minimumDeleteSum_iterative(s1="sea", s2="eat"))

# basically the same as minimum edit distance
# slow recursive solution
from functools import cache


def minimumDeleteSum(s1: str, s2: str) -> int:
    s1 += "."  # add common letter at the end of each word
    s2 += "."
    n, m = len(s1), len(s2)
    s1 = list(map(lambda x: ord(x), list(s1)))  # convert strings to ascii value list
    s2 = list(map(lambda x: ord(x), list(s2)))

    @cache
    def solve(i, j):
        if i == n and j == m:  # matched words
            return 0
        if i == n or j == m:  # didn't match words
            return float('inf')

        if s1[i] == s2[j]:
            return solve(i + 1, j + 1)
        return min(solve(i + 1, j) + s1[i], solve(i, j + 1) + s2[j])

    return solve(0, 0)
