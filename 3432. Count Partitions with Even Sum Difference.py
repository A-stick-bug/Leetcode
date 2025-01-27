def countPartitions(nums: list[int]) -> int:
    total = 0
    for i in range(len(nums) - 1):
        left = sum(nums[:i + 1])
        right = sum(nums[i + 1:])
        total += (right - left) % 2 == 0
    return total


print(countPartitions(nums=[10, 10, 3, 7, 6]))
print(countPartitions(nums=[1, 2, 2]))
print(countPartitions(nums=[2, 4, 6, 8]))
