# ⭐ hard question, worth reviewing
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
# monotonic queue with prefix sum
#
# for each index, we want to remove as many prefix elements as possible to reduce the subarray's size
# however, we must also ensure that the remaining elements still sum up to more than k
# similar to first greater element (also uses deque)

from collections import deque


def shortestSubarray(nums: list[int], k: int) -> int:
    q = deque([(0, -1)])  # (prefix sum up to index (inclusive), index)
    cur = 0
    res = float('inf')

    for right in range(len(nums)):
        cur += nums[right]
        while q and cur - q[0][0] >= k:  # remove extra elements so the remaining is still more than k
            res = min(res, right - q.popleft()[1])

        # remove > elements since we might as well remove everything up to the current if it will result in a GREATER
        # sum, note the >= because even if we remove the same amount, it is more optimal to remove more elements
        while q and q[-1][0] >= cur:
            q.pop()
        q.append((cur, right))  # add the current prefix as an option to remove

    return res if res != float('inf') else -1


print(shortestSubarray(nums=[1], k=1))

# alternate (slower) solution using Fenwick Tree
from itertools import accumulate


class MaxFenwickTree:  # uses 1-indexing
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [-1000000] * (size + 1)

    def update(self, i: int, val: int) -> None:
        """Set self.bit[i] to val"""
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += i & (-i)

    def query(self, i: int):
        """Get the max up to the i-th element (inclusive)"""
        total = -1000000
        while i > 0:
            total = max(total, self.bit[i])
            i -= i & (-i)
        return total


def shortestSubarray(nums: list[int], k: int) -> int:
    # coordinate compression
    vals = [0]
    for i in accumulate(nums):
        vals.append(i)
        vals.append(i - k)
    vals = sorted(set(vals))
    comp = {vals[i]: i + 1 for i in range(len(vals))}

    bit = MaxFenwickTree(len(vals))  # bit[i]: max index with sum of i
    bit.update(comp[0], -1)  # option to remove nothing
    cur = 0  # current prefix sum
    res = 1000000

    for i in range(len(nums)):
        cur += nums[i]
        prev = bit.query(comp[cur - k])  # query max index where the sum is more than K
        res = min(res, i - prev)
        bit.update(comp[cur], i)

    return res if res == 1000000 else -1


print(shortestSubarray([2, -1, 2], 3))
