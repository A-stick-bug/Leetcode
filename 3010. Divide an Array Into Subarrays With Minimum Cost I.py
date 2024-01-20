def minimumCost(nums: list[int]) -> int:
    total = 0
    total += nums[0]
    nums.pop(0)
    nums.sort()
    total += nums[0] + nums[1]
    return total
