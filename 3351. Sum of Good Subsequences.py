# https://leetcode.com/problems/sum-of-good-subsequences
# Subsequence DP
# cnt[num]: number of subsequences ending with num
# total[num]: sum of all subsequences ending with num

from collections import defaultdict


def sumOfGoodSubsequences(nums: list[int]) -> int:
    MOD = 10 ** 9 + 7
    cnt = defaultdict(int)
    total = defaultdict(int)

    cnt[nums[0]] = 1  # base case
    total[nums[0]] = nums[0]

    for num in nums[1:]:
        # consider subsequence building on top of previous ones
        cnt[num] += cnt[num - 1]
        total[num] += total[num - 1] + num * cnt[num - 1]

        cnt[num] += cnt[num + 1]
        total[num] += total[num + 1] + num * cnt[num + 1]

        # consider subsequence start here
        total[num] += num
        cnt[num] += 1

        total[num] %= MOD
        cnt[num] %= MOD

    return sum(total.values()) % MOD


print(sumOfGoodSubsequences([1, 0, 2, 1, 2]))
print(sumOfGoodSubsequences(nums=[1, 2, 1]))
print(sumOfGoodSubsequences(nums=[3, 4, 5]))
