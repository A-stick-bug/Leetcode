def rob(nums):
    if len(nums) == 1:  # edge case
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]  # base cases
    dp[1] = max(nums[1], nums[0])

    for i in range(2, len(nums)):
        # case 1: don't rob this house, case 2: rob it and skip the previous
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]
