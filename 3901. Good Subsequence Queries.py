"""
https://leetcode.com/problems/good-subsequence-queries/description/
Full editorial:
https://leetcode.com/problems/good-subsequence-queries/solutions/7877537/how-to-ignore-length-is-strictly-less-th-r5o4/

Annoying condition: the length of the subsequence is STRICTLY LESS THAN n
Workaround: we can ignore this condition for n > 17:
Reasoning:
Suppose we are finding the GCD of all elements by adding them 1 by 1, there are 2 cases:
- 1) adding it doesn't change the GCD, simply don't take it, and we have found something to exclude
- 2) adding it changes the GCD, by basic math properties, it forces the GCD to at least halve.
     After log2(50000)~17 of these, the GCD will be at 1, and we are forced onto case 1

In other words, if n > 17, there will ALWAYS be something that you can exclude without affecting the GCD.
Note: I know the log is closer to 16 here, but I'm not risking an off by 1 during a contest

TC: O(n*log(n) + q*log(n)*log(m)), O(q * n * log(m)) for small cases
Here, n is the length of the array, m is the max number
"""

from math import ceil, log2, gcd
from itertools import accumulate


class SegTree:
    def __init__(self, arr, f=lambda x, y: x + y, default=0) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        N = len(arr)
        self.f = f  # function used to combine segments
        self.default = default
        self.layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << self.layers
        self.seg = [default] * (2 * self.size)  # 1-indexed, need an extra layer for the actual data

        for i in range(N):  # base layer
            self.seg[self.size + i] = arr[i]
        for i in reversed(range(1, self.size)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])

    def update(self, i, val) -> None:
        """update i-th element to val, 0-indexed"""
        i += self.size  # start from bottom
        self.seg[i] = val
        while i > 1:
            i //= 2
            self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])


def countGoodSubseq(nums: list[int], p: int, queries: list[list[int]]) -> int:
    n = len(nums)

    for i in range(n):
        val = nums[i]
        nums[i] = 0 if val % p != 0 else val // p

    if n <= 17:  # brute force excluding 1 element
        total = 0
        for idx, val in queries:
            nums[idx] = 0 if val % p != 0 else val // p
            pref = [0] + list(accumulate(nums, func=gcd))
            pref.append(pref[-1])
            suf = list(accumulate(nums[::-1], func=gcd))[::-1] + [0]
            suf.insert(0, suf[0])
            if any(gcd(pref[i - 1], suf[i + 1]) == 1 for i in range(1, n + 1)):
                total += 1
        return total

    else:  # no need to exclude 1 element, reasoning is explained above
        seg = SegTree(nums, f=gcd, default=0)
        total = 0
        for idx, val in queries:
            seg.update(idx, 0 if val % p != 0 else val // p)
            if seg.seg[1] == 1:  # root query (gcd over entire array)
                total += 1
        return total
