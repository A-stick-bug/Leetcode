# Using Fenwick Tree for range update and point query
# O(n*log(n))
#
# Index 0 is always reachable (base case)
# Loop through every index (except last) and if the current index is reachable:
#    We can reach the next nums[i] indices from i, so we set those to true (this can be optimized with Fenwick Tree)

from typing import List


class FenwickTree:  # 1-indexed, supports range update and point query
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        i += 1
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def range_add(self, l, r, val):
        self.add(l, val)
        self.add(r + 1, -val)

    def query(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret


def canJump(nums: List[int]) -> bool:
    n = len(nums)
    reachable = FenwickTree(n)
    reachable.range_add(0, 0, 1)  # base case: index 0 is always reachable

    for i in range(n - 1):
        if reachable.query(i):  # if the current index is reachable
            if i + nums[i] + 1 >= n:  # optimization: return early if we can reach end
                return True
            reachable.range_add(i + 1, min(i + nums[i], n - 1), 1)  # we can also reach the next nums[i] indices

    return reachable.query(n - 1) > 0  # return whether we can reach the last index


def brute_force(nums: List[int]) -> bool:
    n = len(nums)
    reachable = [False] * n
    reachable[0] = True

    for i in range(n - 1):
        if reachable[i]:  # range updating like this is too slow
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                reachable[j] = True

    return reachable[-1]
