def maxSubArray(nums) -> int:
    res = -float('inf')
    current = 0  # running total of elements
    for n in nums:
        # if current is negative, reset to 0 because we can just exclude the previous elements
        if current < 0:
            current = n
        else:
            current += n

        res = max(res, current)  # update max value
    return res
