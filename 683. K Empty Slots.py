"""
https://leetcode.com/problems/k-empty-slots/description/

The question statement is quite confusing so let's summarize it first:
- we are adding in bulbs in a certain order
- each time we add something, we check if we created a gap of length K
  - note: ALL bulbs must be off in the gap, so we only need to check (cur - prev) and (next - cur) after adding a bulb

Since Leetcode allows sortedcontainers, we can just use the built-in features of it.

ALTERNATE SOLUTION USING FENWICK TREE BELOW (NO BUILT-INS USED)
"""

from sortedcontainers import SortedList


def kEmptySlots(bulbs: list[int], k: int) -> int:
    turned_on = SortedList()
    for i, cur in enumerate(bulbs, start=1):
        turned_on.add(cur)
        pos = turned_on.index(cur)  # find index to access adjacent elements

        if (pos != 0) and (cur - turned_on[pos - 1] - 1 == k):  # check if gap before contains K
            return i
        if (pos != len(turned_on) - 1) and (turned_on[pos + 1] - cur - 1 == k):  # check if gap after contains K
            return i

    return -1


print(kEmptySlots([6, 5, 8, 9, 7, 1, 10, 2, 3, 4], 2))


# Alternate solution using Fenwick Tree: n*log(n)
# After adding a bulb, we first check if (cur - prev) or (next - cur) has a gap length of K
# We also need to make sure all bulbs are off in between, we can use a Fenwick tree to do this in log(n)


class FenwickTree:  # uses 1-indexing
    def __init__(self, size):
        """Create a Fenwick tree from an array by adding elements one by one"""
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


def kEmptySlots_BIT_solution(bulbs: list[int], k: int) -> int:
    n = len(bulbs)
    bit = FenwickTree(n)
    lights = [0] * (n + 1)

    for i, cur in enumerate(bulbs, start=1):
        bit.update(cur, 1)  # turned light on
        lights[cur] = 1

        prev = cur - k - 1
        after = cur + k + 1
        if prev >= 0 and lights[prev] == 1 and bit.query_range(prev, cur) == 2:
            return i
        if after <= n and lights[after] == 1 and bit.query_range(cur, after) == 2:
            return i

    return -1


print(kEmptySlots_BIT_solution([10, 1, 9, 3, 5, 7, 6, 4, 8, 2], 8))
