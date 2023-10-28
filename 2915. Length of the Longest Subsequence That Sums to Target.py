# DP: variation of longest increasing subsequence

def lengthOfLongestSubsequence(nums, target):
    nums = list(filter(lambda num: num <= target, nums))  # only keep things less than target

    dp = [0] * (target + 1)
    for num in nums:
        for i in reversed(range(target - num + 1)):
            if dp[i] and i + num <= target:
                dp[i + num] = max(dp[i + num], dp[i] + 1)

        if not dp[num]:  # can now get to this number if we couldn't before
            dp[num] = 1

    return dp[target] if dp[target] != 0 else -1


print(lengthOfLongestSubsequence([1, 2, 3, 4, 5], 9))  # 3
print(lengthOfLongestSubsequence([4, 1, 3, 2, 1, 5], 7))  # 4
print(lengthOfLongestSubsequence([1, 1, 5, 4, 5], 3))  # -1
