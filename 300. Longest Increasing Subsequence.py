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


# O(n^2) linear search
def lengthOfLIS(nums) -> int:
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = dp[j] + 1

    return max(dp)


print(lengthOfLIS(nums=[4, 10, 4, 3, 8, 9]))
