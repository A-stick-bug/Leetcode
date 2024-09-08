# https://leetcode.com/problems/reach-end-of-array-with-max-score/
# convex hull trick
# todo: understand this later

from collections import deque


def findMaximumScore(nums):
    n = len(nums)
    dp = [float('-inf')] * n
    dp[0] = 0  # Starting at index 0 with score 0

    # Deque to maintain the lines in a convex hull
    deq = deque([0])

    for j in range(1, n):
        # Remove lines from the deque that are no longer needed
        while len(deq) > 1 and dp[deq[0]] + nums[deq[0]] * (j - deq[0]) <= dp[deq[1]] + nums[deq[1]] * (j - deq[1]):
            deq.popleft()

        # Compute the maximum score for dp[j] using the best line in the convex hull
        i = deq[0]
        dp[j] = dp[i] + (j - i) * nums[i]

        # Maintain the convex hull by removing lines that are no longer useful
        while len(deq) > 1:
            i1, i2 = deq[-2], deq[-1]
            if (dp[i] - dp[i2]) * (i1 - i2) >= (dp[i2] - dp[i1]) * (i - i1):
                deq.pop()
            else:
                break

        deq.append(j)

    return dp[-1]


print(findMaximumScore([1, 3, 1, 5]))
print(findMaximumScore([4, 3, 1, 3, 2]))
