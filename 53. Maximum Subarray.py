def maxSubArray(nums) -> int:
    res = -float('inf')
    current = 0
    for n in nums:
        current = max(n, current + n)  # if current is negative, reset to 0
        res = max(res, current)  # update max value
    return res
