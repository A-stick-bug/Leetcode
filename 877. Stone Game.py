# https://leetcode.com/problems/stone-game/description/
# game theory DP, both people try to maximize their score

from functools import cache


def stoneGame(piles: list[int]) -> bool:
    @cache
    def solve(l, r):
        if l > r:  # out of stones
            return 0
        left = piles[l] - solve(l + 1, r)
        right = piles[r] - solve(l, r - 1)
        return max(left, right)  # both players act optimally, trying to max points

    # we subtract the other person's points, so we win if the net point is more than 0
    return solve(0, len(piles) - 1) > 0


print(stoneGame(piles=[3, 7, 2, 3]))
