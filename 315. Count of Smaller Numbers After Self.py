"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

Template problem for inversion counting
Solution using ranks (coordinate compression) and Fenwick Tree

"""

from typing import List


class FenwickTree:
    def __init__(self, size):
        self.bit = [0] * (size + 1)  # 1-indexed

    def update(self, i, diff):
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total


def countSmaller(nums: List[int]) -> List[int]:
    n = len(nums)
    compress = {val: i for i, val in enumerate(sorted(set(nums)))}  # 0-indexed ranks
    bit = FenwickTree(n)

    res = [0] * n
    for i in reversed(range(n)):
        rank = compress[nums[i]]
        res[i] += bit.query(rank)
        bit.update(rank + 1, 1)
    return res


print(countSmaller([5,2,6,1]))
