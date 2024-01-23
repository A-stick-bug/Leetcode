# not the most efficient solution, just using this to test my seg trees

from math import log2, ceil
from collections import defaultdict


class LazySegTree:  # update to value
    def __init__(self, N, f=lambda x, y: x + y, default=0) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        self.default = default
        layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << layers

        self.seg = defaultdict(int)  # make seg tree sparse, very slow
        self.lazy = defaultdict(int)

    def push_down(self, i, segment_size):
        """transfer lazy tag from parent to children"""
        if self.lazy[i] == 0:
            return
        self.lazy[i * 2] = self.lazy[i]  # transfer lazy tags
        self.lazy[i * 2 + 1] = self.lazy[i]
        self.seg[i * 2] = self.lazy[i] * segment_size  # update value of segments
        self.seg[i * 2 + 1] = self.lazy[i] * segment_size
        self.lazy[i] = 0

    def update(self, i, l, r, cur_l, cur_r, val) -> None:
        """add diff to [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return
        mid = (cur_l + cur_r) // 2
        if l <= cur_l and cur_r <= r:  # fully inside segment: update lazily
            self.lazy[i] = val
            self.seg[i] = (cur_r - cur_l + 1) * val
            return
        self.push_down(i, cur_r - mid)  # partial covers, recurse deeper
        self.update(i * 2, l, r, cur_l, mid, val)
        self.update(i * 2 + 1, l, r, mid + 1, cur_r, val)
        self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    def query(self, i, l, r, cur_l, cur_r) -> int:
        """query [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return self.default
        if l <= cur_l and cur_r <= r:  # fully inside segment
            return self.seg[i]

        mid = (cur_l + cur_r) // 2  # traverse down further
        self.push_down(i, cur_r - mid)
        return self.f(self.query(i * 2, l, r, cur_l, mid),
                      self.query(i * 2 + 1, l, r, mid + 1, cur_r))

    def query_range(self, l, r):
        return self.query(1, l, r, 0, self.size - 1)

    def update_range(self, l, r, diff):
        return self.update(1, l, r, 0, self.size - 1, diff)


class CountIntervals:
    def __init__(self):
        self.MN = 10 ** 9 + 1
        self.seg = LazySegTree(self.MN)

    def add(self, left: int, right: int) -> None:
        self.seg.update_range(left, right, 1)

    def count(self) -> int:
        return self.seg.query_range(0, self.MN)
