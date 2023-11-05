# variation of LIS, with an extra variable
# time complexity O(n^2)

def longestArithSeqLength(nums: list[int]) -> int:
    n = len(nums)
    # dp[i][j] is the longest arithmetic sequence possible using elements up to nums[i] and common difference of (j-500)
    dp = [[1] * 1001 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j] + 500  # make the common difference positive
            dp[i][diff] = dp[j][diff] + 1
    return max(max(row) for row in dp)  # get maximum possible


print(longestArithSeqLength(nums=[20, 1, 15, 3, 10, 5, 8]))
