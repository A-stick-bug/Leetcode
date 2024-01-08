# general 1D DP
# reach current state from previous states


def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    dp = [0] * (high + 1)
    dp[0] = 1  # base case: there is always 1 way to have nothing

    for i in range(1, high + 1):
        if i - one >= 0:
            dp[i] += dp[i - one] % 1_000_000_007  # taking mod here keeps the number reasonably small (faster)
        if i - zero >= 0:
            dp[i] += dp[i - zero] % 1_000_000_007
    return sum(dp[low:high + 1]) % 1_000_000_007


print(countGoodStrings(low=3, high=3, zero=1, one=1))
