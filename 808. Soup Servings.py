# https://leetcode.com/problems/soup-servings/
# Probability DP with a trick
# Because on average, more A soup is removed, as n grows large, A will almost certainly be empty first
# Note: The question allows a relative error of 10^-5

from functools import cache

def soupServings(n: int) -> float:
    if n > 10000:  # if n is this large, the answer is close enough to 1 (difference is less than 10^-5)
        return 1
    soup = [(100, 0), (75, 25), (50, 50), (25, 75)]

    @cache
    def solve(a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0
        return sum(solve(a - remove_a, b - remove_b) for remove_a, remove_b in soup)*0.25

    return solve(n, n)
