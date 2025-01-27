def subarraySum(nums: list[int]) -> int:
    total = 0
    for i in range(len(nums)):
        total += sum(nums[max(0, i - nums[i]):i + 1])
    return total
