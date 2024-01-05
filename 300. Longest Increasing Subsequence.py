# https://leetcode.com/problems/longest-increasing-subsequence/
# fun problem with many solutions, such as greedy, DP, and using data structures
#
# this is one of the few times we get to use a Max Fenwick Tree
# at the i-th iteration, bit has everything before the current element
# querying the bit will return the maximum element in [1:i], 1-indexed

class FenwickTree:  # uses 1-indexing
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, val: int) -> None:
        """Set self.bit[i] to val"""
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += i & (-i)

    def query(self, i: int):
        """Get the max up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total = max(total, self.bit[i])
            i -= i & (-i)
        return total


def LIS_with_BIT(nums: list[int]) -> int:
    n = len(nums)
    ordered = sorted(set(nums))
    compress = {ordered[i]: i + 1 for i in range(n)}  # coordinate compress to 1-indexed

    bit = FenwickTree(len(ordered))
    for num in nums:
        num = compress[num]  # only relative order matters
        best = bit.query(num - 1)  # get the greatest LIS from numbers smaller than the current
        bit.update(num, best + 1)  # +1 to add current element to LIS

    return bit.query(len(ordered))


print(LIS_with_BIT(nums=[10, 9, 2, 5, 3, 7, 101, 18]))

#################################################################
# O(n*log(n)) greedy approach using binary search
from bisect import bisect_left


def fasterLIS(nums) -> int:
    res = []
    for n in nums:
        i = bisect_left(res, n)
        if i == len(res):  # current element is largest
            res.append(n)
        else:
            res[i] = n

    return len(res)


###############################################################
# O(n^2) linear search
def lengthOfLIS(nums) -> int:
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = dp[j] + 1

    return max(dp)
