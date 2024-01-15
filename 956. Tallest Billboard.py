# ⭐ WORTH REVIEWING FOR SURE
# https://leetcode.com/problems/tallest-billboard
# Simplify problem: for each rod, we multiply by one of [-1, 0, 1]
# 1: put in first support, 0: don't use, 1: put in second support
# out goal is to reach a sum of 0

from functools import cache


def tallestBillboard(rods: list[int]) -> int:
    n = len(rods)

    @cache
    def solve(i, cur):
        if i == n:
            if cur == 0:
                return 0
            else:
                return -(1 << 30)
        return max(rods[i] + solve(i + 1, cur + rods[i] * -1),
                   solve(i + 1, cur),
                   rods[i] + solve(i + 1, cur + rods[i] * 1))

    return solve(0, 0) // 2


print(tallestBillboard(rods=[1, 2, 3, 4, 5, 6]))


# brute force (TLE): partition rods into 3 subsets: unused, support 1, and support 2
def tallestBillboard_brute_force(rods: list[int]) -> int:
    n = len(rods)

    def solve(i, s1, s2, s3):
        if i == n:
            t1, t2 = sum(s2), sum(s3)
            return (t1 == t2) * t1
        return max(solve(i + 1, s1, s2, s3.union({rods[i]})),
                   solve(i + 1, s1, s2.union({rods[i]}), s3),
                   solve(i + 1, s1.union({rods[i]}), s2, s3))

    return solve(0, set(), set(), set())
