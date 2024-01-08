# https://leetcode.com/problems/unique-binary-search-trees
# tree DP with some math

from functools import cache


def numTrees(n: int) -> int:
    @cache
    def solve(l, r):
        if l >= r:  # valid subtree
            return 1

        total = 0
        for i in range(l, r+1):  # try all split points as the root
            total += solve(l, i - 1) * solve(i + 1, r)  # multiply left and right
        return total

    return solve(1, n)


print(numTrees(1))
