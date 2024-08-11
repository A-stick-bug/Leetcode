# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii
# Simple DP optimization with prefix sum
# states: current index, current number
# TC: O(NM)

from itertools import accumulate


def countOfPairs(nums: list[int]) -> int:
    n = len(nums)
    m = max(nums) + 1
    MOD = 10 ** 9 + 7
    dp = [[0] * m for _ in range(n)]

    # base cases: valid first numbers
    for i in range(m):
        dp[0][i] = 1 if i <= nums[0] else 0

    for idx in range(1, n):
        prev_psa = [0] + list(accumulate(dp[idx - 1]))
        query = lambda l, r: prev_psa[r + 1] - prev_psa[l]  # query range on previous row
        for num in range(m):
            other = nums[idx] - num
            if other < 0:  # all numbers must be non-negative
                continue
            l = 0
            r = min(num, nums[idx - 1] - other)  # ensure other array is descending
            if l <= r:
                dp[idx][num] = query(l, r) % MOD

    return sum(dp[-1]) % MOD


print(countOfPairs([5, 5, 5, 5]))
