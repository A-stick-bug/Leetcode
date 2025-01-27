# https://leetcode.com/problems/maximum-frequency-after-subarray-operation
# - Simplify the question to max subarray sum for each number
# - For each number in [1,50], we try turning it into `k` while
#   also minimizing modifications to already existing `k` values

def maxFrequency(nums: list[int], k: int) -> int:
    freq_k = nums.count(k)
    res = freq_k

    for i in range(1, 51):
        arr = []
        for val in nums:
            if val == k:
                arr.append(-1)
            elif val == i:
                arr.append(1)

        # max subarray sum, Kadane's algorithm
        cur = best = 0
        for val in arr:
            cur += val
            best = max(best, cur)
            cur = max(0, cur)
        res = max(res, best + freq_k)

    return res


print(maxFrequency(nums=[1, 2, 3, 4, 5, 6], k=1))
print(maxFrequency(nums=[10, 2, 3, 4, 5, 5, 4, 3, 2, 2], k=10))
