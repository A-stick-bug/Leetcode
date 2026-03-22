# https://leetcode.com/problems/minimum-removals-to-achieve-target-xor
# Knapsack DP

def minRemovals(nums: list[int], target: int) -> int:
    n = len(nums)
    inf = 1 << 30

    # nums^removals = target -> removals = target^nums
    for i in nums:
        target ^= i

    # find minimum number of elements that XOR to target
    mx = max(nums)
    mx_bit = 1 << mx.bit_length()
    if target >= mx_bit:
        return -1

    dp = [inf] * mx_bit  # dp[X] = minimum numbers to reach X

    dp[0] = 0
    for val in nums:
        new_dp = dp.copy()
        for i in range(mx_bit):
            new_dp[i] = min(new_dp[i], dp[i ^ val] + 1)
        dp = new_dp

    return dp[target] if dp[target] != inf else -1
