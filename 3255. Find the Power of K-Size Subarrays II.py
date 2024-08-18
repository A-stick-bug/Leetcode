# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii
# Data structures spam
# use prefix sum to check for consecutive
# use sparse table to query max

from itertools import accumulate
import sys

log2 = lambda x: x.bit_length() - 1


class SparseTable:  # 0-indexed
    def __init__(self, arr, f=max, default=0):
        N = len(arr)
        self.layers = log2(len(arr)) + 1
        self.table = [[default] * self.layers for _ in range(len(arr))]
        self.f = f
        for i in range(len(arr)):  # base layer
            self.table[i][0] = arr[i]  # column 1: base cases

        for k in range(1, self.layers):  # build the rest of the table
            for i in range(N - (1 << k) + 1):
                self.table[i][k] = f(self.table[i][k - 1], self.table[i + (1 << (k - 1))][k - 1])

    def query(self, l, r):
        k = log2(r - l + 1)
        return self.f(self.table[l][k], self.table[r - (1 << k) + 1][k])


def resultsArray(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    asc = [nums[i] + 1 == nums[i + 1] for i in range(n - 1)]
    psa = [0] + list(accumulate(asc))
    query = lambda l, r: psa[r] - psa[l]

    st = SparseTable(nums, f=max, default=0)
    res = []

    for l in range(n - k + 1):
        r = l + k - 1
        if query(l, r) == k - 1:
            res.append(st.query(l, r))
        else:
            res.append(-1)
    return res


print(resultsArray(nums=[1, 2, 3, 4, 3, 2, 5], k=3))
print(resultsArray(nums=[2, 2, 2, 2, 2], k=4))
print(resultsArray(nums=[3, 2, 3, 2, 3, 2], k=2))
