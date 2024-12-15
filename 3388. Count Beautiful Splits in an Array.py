# https://leetcode.com/problems/count-beautiful-splits-in-an-array
# Any string matching algorithm works
# I used hashing because it's the simplest
# Note: apparently the intended solution is dynamic programming?

from itertools import accumulate


def beautifulSplits(nums: list[int]) -> int:
    n = len(nums)
    if n < 3:  # edge case: no valid splits
        return 0

    MOD = 177635683940025046467781066894531
    p = 53  # p should be greater than max(nums)

    power = [0] * n  # precompute powers of `p`, with MOD
    power[0] = 1
    for i in range(1, n):
        power[i] = (power[i - 1] * p) % MOD

    hash1 = [0] * n  # precompute hashes of each character in `str1`
    for i in range(n):
        hash1[i] = (nums[i] * power[n - i - 1]) % MOD
    psa1 = [0] + list(accumulate(hash1))  # psa for range hash query

    total = 0
    for end1 in range(n):
        for end2 in range(end1 + 1, n - 1):
            # formula for substring hash: (psa1[r1 + 1] - psa1[l1]) * power[l1] % MOD

            # check A is prefix of B
            l1 = 0
            r1 = end1
            l2 = end1 + 1
            r2 = end2
            if (r1 - l1) <= (r2 - l2):  # check prefix
                r2 = l2 + r1
                hash1 = (psa1[r1 + 1] - psa1[l1]) * power[l1] % MOD  # shift up
                hash2 = (psa1[r2 + 1] - psa1[l2]) * power[l2] % MOD
                if hash1 == hash2:
                    total += 1
                    continue

            # check B is prefix of C
            l1 = end1 + 1
            r1 = end2
            l2 = end2 + 1
            r2 = n - 1
            if (r1 - l1) <= (r2 - l2):  # check prefix
                r2 = l2 + (r1 - l1 + 1) - 1
                hash1 = (psa1[r1 + 1] - psa1[l1]) * power[l1] % MOD  # shift up
                hash2 = (psa1[r2 + 1] - psa1[l2]) * power[l2] % MOD
                if hash1 == hash2:
                    total += 1

    return total


print(beautifulSplits([2, 3, 2, 2, 1]))
print(beautifulSplits(nums=[1, 1, 2, 1]))
print(beautifulSplits(nums=[1, 2, 3, 4]))
