# Knapsack DP
# storing 2 states: number of 0 and 1 remaining

from functools import cache


# bottom-up approach
def bottom_up(strs: list[str], m: int, n: int):
    count = [(s.count("0"), s.count("1")) for s in strs]
    dp = [[0] * 101 for _ in range(101)]
    for zero, one in count:
        for i in reversed(range(zero, m + 1)):  # iterate in reverse to prevent duplicating values
            for j in reversed(range(one, n + 1)):
                dp[i][j] = max(1 + dp[i - zero][j - one], dp[i][j])
    return dp[m][n]


def findMaxForm(strs: list[str], m: int, n: int) -> int:
    count = [(s.count("0"), s.count("1")) for s in strs]

    @cache
    def solve(i, zero, one):
        # if we went below zero, it means the previous function call does not give a valid answer, so we much remove 1
        if zero < 0 or one < 0:
            return -1
        if i >= len(strs):  # prevent going out of bounds
            return 0

        # we either use the current string or don't use it
        return max(1 + solve(i + 1, zero - count[i][0], one - count[i][1]), solve(i + 1, zero, one))

    return solve(0, m, n)


print(bottom_up(strs=["10", "0001", "111001", "1", "0"], m=4, n=3))
