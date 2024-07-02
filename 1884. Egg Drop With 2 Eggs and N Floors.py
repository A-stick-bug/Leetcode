"""
https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
Brute force DP
Check out https://leetcode.com/problems/super-egg-drop for general solution (and more efficient)

Observations:
- once we break the first egg, we must try floors consecutively using the second one
- DP state: [low], we currently know the egg does not break at low (or anything below)

TC: O(n^2), n state, O(n) transitions
"""

from functools import cache


def twoEggDrop(n: int) -> int:
    @cache
    def solve(low):
        if low >= n:  # base case: egg didn't break on top floor
            return 0
        ans = 10000
        for drop in range(low + 1, n + 1):
            # if it broke, we use second egg to try all floor from the currently known
            # lower bound to the current floor
            broke = drop - low
            # otherwise, update the currently known lower bound to the current floor
            not_broke = solve(drop) + 1
            ans = min(ans, max(broke, not_broke))
        return ans

    return solve(0)


print(twoEggDrop(2))
print(twoEggDrop(100))
