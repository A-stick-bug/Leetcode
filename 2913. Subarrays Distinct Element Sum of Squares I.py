from collections import Counter


def sumCounts(nums: list[int]) -> int:
    total = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            total += len(Counter(nums[i:j])) ** 2
    return total
