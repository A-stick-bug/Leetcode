"""
https://leetcode.com/problems/find-median-from-data-stream/description/
(Not optimal) Solution using an Order Statistic Tree (implemented using Fenwick Tree)

Query: (log(n))
Update: O(log(n))

"""


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res

    def select(self, k):  # binary search to get k-th element
        i = 0
        bit_length = self.size.bit_length()
        for _ in range(bit_length, -1, -1):
            if i + (1 << _) <= self.size and self.tree[i + (1 << _)] < k:
                i += 1 << _
                k -= self.tree[i]
        return i + 1


class MedianFinder:
    def __init__(self):
        self.bit = FenwickTree(200_002)  # include negative values as well
        self.MAX = 100_001
        self.nums = 0

    def addNum(self, num: int) -> None:
        self.bit.update(num + self.MAX, 1)  # add value as positive
        self.nums += 1

    def findMedian(self) -> float:
        if self.nums % 2 == 1:  # odd number has 1 median
            i = self.nums // 2 + 1
            return self.bit.select(i) - self.MAX

        else:  # even number has 2 medians, take the average
            i = self.nums // 2
            return (self.bit.select(i) + self.bit.select(i + 1) - self.MAX - self.MAX) / 2
