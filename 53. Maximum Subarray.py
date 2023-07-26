def maxSubArray(nums) -> int:
    res = -float('inf')
    current = 0
    for i in range(len(nums)):
        current = max(nums[i], current+nums[i])  # if current is negative, reset to 0
        res = max(res, current)  # update max value
    return res
