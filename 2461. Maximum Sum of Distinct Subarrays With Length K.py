# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
# typical sliding window question

from collections import Counter


def maximumSubarraySum(nums: list[int], k: int) -> int:
    n = len(nums)
    cur_sum = 0
    freq = Counter()
    best = 0

    for i in range(n):
        freq[nums[i]] += 1
        cur_sum += nums[i]
        if i >= k - 1:
            if len(freq) == k:
                best = max(best, cur_sum)
            l = i - k + 1
            cur_sum -= nums[l]
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]

    return best


print(maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3))
print(maximumSubarraySum(nums=[4, 4, 4], k=3))
