# https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/description/
# Subsequence DP, transition with segment tree
# track dp[val][up/down] = maximum length subsequence ending with val that goes up/down
# delay updates until k indices later to ensure gaps

from math import ceil, log2


class SegTree:
    def __init__(self, arr, f=lambda x, y: x + y, default=0) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        self.default = default
        N = len(arr)
        self.N = N
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
        self.seg[i] = max(self.seg[i], val)
        while i > 1:
            i //= 2
            self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    def query(self, left, right):
        if left > right:
            return self.default
        left = max(0, left)
        right = min(self.N - 1, right)
        left += self.size
        right += self.size + 1

        res_left = res_right = self.default
        while left < right:
            if left & 1:  # left is odd
                res_left = self.f(res_left, self.seg[left])
                left += 1
            if right & 1:
                right -= 1
                res_right = self.f(self.seg[right], res_right)
            left //= 2
            right //= 2
        return self.f(res_left, res_right)


def maxAlternatingSum(nums: list[int], k: int) -> int:
    ordered = sorted(set(nums))
    m = len(ordered)
    compress = {ordered[i]: i for i in range(m)}
    arr = [compress[i] for i in nums]
    n = len(arr)

    dp_up = SegTree([0] * m, f=max, default=0)
    dp_down = SegTree([0] * m, f=max, default=0)

    pending_up = [-1] * n
    pending_down = [-1] * n
    pending_up[0] = pending_down[0] = nums[0]
    for i in range(1, n):
        if i - k >= 0:
            dp_up.update(arr[i - k], pending_up[i - k])
            dp_down.update(arr[i - k], pending_down[i - k])
        pending_up[i] = nums[i] + dp_down.query(0, arr[i] - 1)
        pending_down[i] = nums[i] + dp_up.query(arr[i] + 1, n - 1)

    return max(max(pending_up), max(pending_down))


print(maxAlternatingSum(nums=[5, 4, 2], k=2))
print(maxAlternatingSum(nums=[3, 5, 4, 2, 4], k=1))
print(maxAlternatingSum(nums=[5], k=1))
