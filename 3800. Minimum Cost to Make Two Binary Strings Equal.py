# https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal
# Make observations and use greedy
# We don't prove anything, but it intuitively makes sense
#
# observations:
# - crossing by itself does nothing
#   - always use with swapping
# - never touch already matched

def minimumCost(s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
    cost = 0
    z_dif = sum(i == "0" and j == "1" for i, j in zip(s, t))
    o_dif = sum(i == "1" and j == "0" for i, j in zip(s, t))
    mi = min(z_dif, o_dif)
    rest = z_dif + o_dif
    if swapCost < 2 * flipCost:  # swap to equalize pairs
        z_dif -= mi
        o_dif -= mi
        cost += mi * swapCost
        rest -= 2 * mi

        if swapCost + crossCost < 2 * flipCost:  # cross + swap to equalize pairs
            groups = rest // 2 * 2
            cost += groups // 2 * (swapCost + crossCost)
            rest -= groups
    return cost + rest * flipCost
