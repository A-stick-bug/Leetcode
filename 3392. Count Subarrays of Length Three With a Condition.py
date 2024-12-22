def countSubarrays(nums: list[int]) -> int:
    n = len(nums)
    total = 0
    for i in range(n - 2):
        total += (nums[i + 1] == 2 * nums[i] + 2 * nums[i + 2])
    return total
