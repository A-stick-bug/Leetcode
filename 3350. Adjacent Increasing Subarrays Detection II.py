# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/
# PSA + binary search
# note: there probably exists simpler solutions

from itertools import accumulate


def maxIncreasingSubarrays(nums: list[int]) -> int:
    def works(m):
        for i in range(n - 2 * m + 1):
            l = i
            r = i + m - 1
            l2 = r + 1
            r2 = l2 + m - 1
            if 0 == query(l, r) == query(l2, r2):
                return True
        return False

    n = len(nums)
    dec = [nums[i] >= nums[i + 1] for i in range(n - 1)] + [0]
    psa = [0] + list(accumulate(dec))
    query = lambda l, r: psa[r] - psa[l]

    low = 0
    high = n // 2
    while low <= high:
        mid = (low + high) // 2
        if works(mid):
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


print(maxIncreasingSubarrays(nums=[1, 2, 3, 2, 3, 4]))
print(maxIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
print(maxIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
