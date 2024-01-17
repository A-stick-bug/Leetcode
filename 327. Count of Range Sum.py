"""
⭐ DIFFICULT QUESTION
https://leetcode.com/problems/count-of-range-sum/

Keep track of the prefix sums in a sorted list.
For each element, we can now find the minimum number of elements we can not include to have a sum of upper
and the maximum number of elements we can not include to have a sum of lower
^ to do this efficiently, we can use sortedlist or Fenwick Tree + coordinate compression
"""

from sortedcontainers import SortedList


def countRangeSum(nums: list[int], lower: int, upper: int) -> int:
    sums = SortedList([0])  # zero is there because we can just take the element itself as a range
    cur = 0
    total = 0

    for num in nums:
        cur += num  # add current number to prefix sum

        # (cur-upper) is the stuff we can remove from before so that after we remove it,
        # we are left with a sum as coe as possible to but above the lower bound
        # (cur-lower) is the opposite
        low = sums.bisect_left(cur - upper)
        high = sums.bisect_right(cur - lower)
        total += high - low

        sums.add(cur)

    return total


# alternate solution using Fenwick Tree
# basically the exact same as the above solution, but we write our own sortedlist
from itertools import accumulate


class FenwickTree:  # uses 1-indexing
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: int) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total

    def query_range(self, left, right):
        """Query the sum of elements from left to right, inclusive"""
        return self.query(right) - self.query(left - 1)


def countRangeSum2(nums: list[int], lower: int, upper: int) -> int:
    psa = [0] + list(accumulate(nums))

    # coordinate compression, we must make sure to include all possible compressible values
    ordered = set()
    for i in psa:
        ordered.add(i)
        ordered.add(i - lower)
        ordered.add(i - upper)
    ordered = sorted(ordered)
    compress = {ordered[i]: i + 1 for i in range(len(ordered))}

    total = 0
    bit = FenwickTree(len(ordered))
    bit.update(compress[0], 1)

    for cur in psa[1:]:
        # (cur-upper) is the stuff we can remove from before so that after we remove it,
        # we are left with a sum as coe as possible to but above the lower bound
        # (cur-lower) is the opposite
        total += bit.query_range(compress[cur - upper], compress[cur - lower])

        bit.update(compress[cur], 1)  # add current subarray sum as an option

    return total


print(countRangeSum2(nums=[-2, 5, -1], lower=-2, upper=2))
