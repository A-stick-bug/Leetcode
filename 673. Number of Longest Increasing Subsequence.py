# LIS DP with extra count
# we need an extra list to count how many times a number was used in the LIS
# could probably get O(n*log(n)) using data structures

def findNumberOfLIS(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    cnt = [1] * n

    for i, val in enumerate(nums):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[i] < dp[j] + 1:  # longer sequence formed, reset count
                    cnt[i] = cnt[j]
                    dp[i] = dp[j] + 1

                elif dp[i] == dp[j] + 1:  # same length sequence, increase count
                    cnt[i] += cnt[j]

    best = max(dp)
    return sum(cnt[i] for i in range(n) if dp[i] == best)


print(findNumberOfLIS([1, 2, 3, 1, 2, 3]))
