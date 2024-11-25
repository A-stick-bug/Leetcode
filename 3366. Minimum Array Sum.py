# https://leetcode.com/problems/minimum-array-sum/description/
# annoying DP, make sure to not mess up the state transitions

def minArraySum(nums: list[int], k: int, op1: int, op2: int) -> int:
    inf = 1 << 60
    prev = [[inf] * (op2 + 1) for _ in range(op1 + 1)]
    prev[0][0] = 0

    for val in nums:  # apply each index
        dp = [[inf] * (op2 + 1) for _ in range(op1 + 1)]

        for a in range(op1 + 1):
            for b in range(op2 + 1):
                dp[a][b] = prev[a][b] + val  # no operations used
                if a != 0:
                    dp[a][b] = min(dp[a][b],
                                   prev[a - 1][b] + (val + 1) // 2)  # divide once

                if val >= k and b != 0:
                    dp[a][b] = min(dp[a][b],
                                   prev[a][b - 1] + val - k)  # minus k once

                if val >= k and b != 0 and a != 0:
                    dp[a][b] = min(dp[a][b],
                                   prev[a - 1][b - 1] + (val - k + 1) // 2)  # minus k then divide

                if (val + 1) // 2 >= k and a != 0 and b != 0:
                    dp[a][b] = min(dp[a][b],
                                   prev[a - 1][b - 1] + (val + 1) // 2 - k)  # divide then minus k
        prev = [r.copy() for r in dp]

    return min(min(row) for row in dp)


print(minArraySum(nums=[2, 8, 3, 19, 3], k=3, op1=1, op2=1))
print(minArraySum(nums=[2, 4, 3], k=3, op1=2, op2=1))
print(minArraySum([10, 6], 10, 0, 1))
