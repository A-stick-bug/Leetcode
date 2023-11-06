# time complexity: O(n)

from collections import defaultdict

def longestSubsequence(arr: list[int], difference: int) -> int:
    dp = defaultdict(int)
    for i in arr:
        dp[i] = dp[i - difference] + 1
    return max(dp.values())


print(longestSubsequence(  arr = [1,2,3,4], difference = 1))
