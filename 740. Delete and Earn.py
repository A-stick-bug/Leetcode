# counting sort: perfect for this question because max(nums) is small
# an alternative is to use Counter() but will make the code slightly more complicated


def deleteAndEarn(nums) -> int:
    if len(nums) == 1:  # edge case
        return nums[0]

    m = max(nums) + 1
    count = [0] * m
    for i in nums:
        count[i] += i

    dp = [0] * m
    dp[0] = count[0]  # base cases
    dp[1] = max(count[1], count[0])

    for i in range(2, m):
        dp[i] = max(dp[i - 1], count[i] + dp[i - 2])

    return dp[-1]


print(deleteAndEarn(nums=[3, 4, 2]))
