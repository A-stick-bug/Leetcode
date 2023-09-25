"""
https://leetcode.com/problems/reverse-pairs/description/
An inversion counting question but the definition of an inversion changes
- nums[i] > 2 * nums[j]

Solution using Fenwick Tree and coordinate compression
- The numbers can be very big in this question, we need to use coordinate compression
- In other words, get the rank of each element by size

"""

from typing import List


class FenwickTree:  # standard Fenwick Tree implementation, uses 1-indexing
    def __init__(self, size):
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: int) -> None:
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total


def reversePairs(nums: List[int]) -> int:
    all_nums = nums + list(map(lambda x: x * 2, nums))  # make another array with each element times 2
    ordered = sorted(set(all_nums))  # sorted list with all elements and x2

    compress = {ordered[i]: i + 1 for i in range(len(ordered))}  # ranks are 1-indexed
    bit = FenwickTree(len(compress) * 2)

    inversions = 0
    for i in reversed(nums):
        rank = compress[i]
        inversions += bit.query(rank - 1)
        bit.update(compress[i * 2], 1)  # multiply by 2 because "nums[i] > 2 * nums[j]" is an inversion

    return inversions


print(reversePairs([1, 3, 2, 3, 1]))
