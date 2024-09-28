"""
https://leetcode.com/problems/range-module/

Maintain a list of intervals for efficient query and updates
Warning: there is A LOT of casework

Time complexity analysis (amortized):
add range: O(log(n)), each interval is merged at most once
query range: O(log(n)), just binary search
remove range: O(log(n)), each interval is removed at most once
- note that each operation creates at most 1 new interval
"""

from sortedcontainers import SortedList

inf = 1 << 30


class RangeModule:
    def __init__(self):
        # list of disjoint intervals [l,r], first add padding to prevent index errors
        self.intervals = SortedList([[-inf, -inf], [inf, inf]])

    def addRange(self, left: int, right: int) -> None:
        """Mark [left, right) as true"""
        right -= 1  # inclusive
        idx = self.intervals.bisect_right([left, inf])  # find index based on left

        # merge interval to the left, overlaps with at most 1
        if self.intervals[idx - 1][1] + 1 >= left:  # extend previous
            self.intervals[idx - 1][1] = max(self.intervals[idx - 1][1], right)
            idx -= 1
        else:  # insert new
            self.intervals.add([left, right])

        # merge intervals to the right, can overlap with many
        while idx + 1 < len(self.intervals) and self.intervals[idx + 1][0] <= right + 1:
            self.intervals[idx][1] = max(self.intervals[idx][1], self.intervals.pop(idx + 1)[1])

    def queryRange(self, left: int, right: int) -> bool:
        """Check if everything in [left, right) is true"""
        right -= 1  # inclusive
        idx = self.intervals.bisect_right([left, inf]) - 1
        return self.intervals[idx][0] <= left <= right <= self.intervals[idx][1]

    def removeRange(self, left: int, right: int) -> None:
        """Mark [left, right) as false"""
        right -= 1  # inclusive
        idx = self.intervals.bisect_right([left, inf]) - 1

        # remove intervals to the right, can remove many
        while idx + 1 < len(self.intervals) and self.intervals[idx + 1][0] <= right:
            if self.intervals[idx + 1][1] <= right:  # fully covered
                self.intervals.pop(idx + 1)
            else:  # cut left
                self.intervals[idx + 1][0] = max(self.intervals[idx + 1][0], right + 1)

        # remove interval to the left, removes at most 1
        l, r = self.intervals[idx]
        if r < left:  # no overlap
            return
        elif l == left:  # cut left
            self.intervals[idx][0] = right + 1
        elif left <= l and r <= right:  # full remove
            self.intervals.pop(idx)
        elif l < left <= right < r:  # cut interval in half
            self.intervals.pop(idx)
            self.intervals.add([l, left - 1])
            self.intervals.add([right + 1, r])
        else:  # cut right
            self.intervals[idx][1] = left - 1


rangeModule = RangeModule()

print(rangeModule.addRange(10, 20))
print(rangeModule.removeRange(14, 16))
print(rangeModule.queryRange(10, 14))  # return True,(Every number in [10, 14) is being tracked)
print(rangeModule.queryRange(13, 15))  # return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
print(rangeModule.queryRange(16,
                             17))  # return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)

# # Solution 2:
# # dynamic lazy seg tree that updates by SETTING A RANGE TO A VALUE
# # same time complexities as solution 1
#
# from math import log2, ceil
# from collections import defaultdict
#
#
# class LazySegTree2:  # update to value
#     def __init__(self, N, f=lambda x, y: x + y, default=0) -> None:
#         """create 1-indexed segment tree from 0-indexed array"""
#         self.f = f  # function used to combine segments
#         self.default = default
#         layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
#         self.size = 1 << layers
#
#         self.seg = defaultdict(int)  # make seg tree sparse, very slow
#         self.lazy = defaultdict(int)
#
#     def push_down(self, i, segment_size):
#         """transfer lazy tag from parent to children"""
#         if self.lazy[i] == 0:
#             return
#         self.lazy[i * 2] = self.lazy[i]  # transfer lazy tags
#         self.lazy[i * 2 + 1] = self.lazy[i]
#         self.seg[i * 2] = self.lazy[i] * segment_size  # update value of segments
#         self.seg[i * 2 + 1] = self.lazy[i] * segment_size
#         self.lazy[i] = 0
#
#     def update(self, i, l, r, cur_l, cur_r, val) -> None:
#         """add diff to [left, right]"""
#         if cur_r < l or r < cur_l:  # fully outside segment
#             return
#         mid = (cur_l + cur_r) // 2
#         if l <= cur_l and cur_r <= r:  # fully inside segment: update lazily
#             self.lazy[i] = val
#             self.seg[i] = (cur_r - cur_l + 1) * val
#             return
#         self.push_down(i, cur_r - mid)  # partial covers, recurse deeper
#         self.update(i * 2, l, r, cur_l, mid, val)
#         self.update(i * 2 + 1, l, r, mid + 1, cur_r, val)
#         self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])
#
#     def query(self, i, l, r, cur_l, cur_r) -> int:
#         """query [left, right]"""
#         if cur_r < l or r < cur_l:  # fully outside segment
#             return self.default
#         if l <= cur_l and cur_r <= r:  # fully inside segment
#             return self.seg[i]
#
#         mid = (cur_l + cur_r) // 2  # traverse down further
#         self.push_down(i, cur_r - mid)
#         return self.f(self.query(i * 2, l, r, cur_l, mid),
#                       self.query(i * 2 + 1, l, r, mid + 1, cur_r))
#
#     def query_range(self, l, r):
#         return self.query(1, l, r, 0, self.size - 1)
#
#     def update_range(self, l, r, diff):
#         return self.update(1, l, r, 0, self.size - 1, diff)
#
#
# class RangeModule:
#     def __init__(self):
#         self.seg = LazySegTree2(10 ** 9 + 1)
#
#     def addRange(self, left: int, right: int) -> None:
#         self.seg.update_range(left, right, 1)
#
#     def queryRange(self, left: int, right: int) -> bool:
#         return (right - left + 1) == self.seg.query_range(left, right)
#
#     def removeRange(self, left: int, right: int) -> None:
#         self.seg.update_range(left, right, 0)
