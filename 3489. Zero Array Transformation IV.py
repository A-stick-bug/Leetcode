# https://leetcode.com/problems/zero-array-transformation-iv/description/
# Simplifies to binary search + knapsack dp (subset sum problem)
# Optimize with bitmask for 32x knapsack speedup
# TC: O(1/32 * logQ * N * Q * MN)

from typing import List


def minZeroArray(nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)

    def works(mid):
        q = queries[:mid]
        for i in range(n):
            dp = 1
            for l, r, v in q:  # knapsack
                if l <= i <= r:
                    dp |= dp << v
            if not dp & (1 << nums[i]):
                return False
        return True

    low = 0
    high = len(queries)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if works(mid):
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans
