# just implementation

def maxOperations(nums: list[int]) -> int:
    total = 1
    sc = nums[0] + nums[1]
    for i in range(2, len(nums) - 1, 2):
        if nums[i] + nums[i + 1] == sc:
            total += 1
        else:
            break
    return total


print(maxOperations(nums=[3, 2, 1, 4, 5]))
