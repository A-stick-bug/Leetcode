# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/description/
# Greedy and math
# - first, notice that dividing by the largest proper divisor just results in
#   a number turning into it's smallest proper divisor
# - in other words, this operation can only be done once
# - greedy idea: start from the end and only use this operation when we need
# - precompute the smallest proper divisors of all numbers up to 10^6 using sieve

MN = 10 ** 6 + 1
inf = 1 << 30
smallest = [inf] * MN
for i in range(2, MN):  # sieve
    if smallest[i] != inf:
        continue
    for j in range(i + i, MN, i):
        smallest[j] = min(smallest[j], i)


def minOperations(nums: list[int]) -> int:
    total = 0
    for i in reversed(range(len(nums) - 1)):
        if nums[i] > nums[i + 1]:  # must decrease current number to keep non-decreasing
            if smallest[nums[i]] > nums[i + 1]:  # still doesn't work
                return -1
            nums[i] = smallest[nums[i]]
            total += 1
    return total


print(minOperations([1, 1, 1]))
