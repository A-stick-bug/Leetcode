# https://leetcode.com/problems/solving-questions-with-brainpower/
# classic take it or leave it DP question, but in reverse
# if we take it, we get score but must skip the next x questions, if we leave it, just move on to the next
# it is easier to skip the previous x questions instead of the next, so we iterate in reverse

def mostPoints(questions: list[list[int]]) -> int:
    n = len(questions)
    dp = [0] * n
    dp[-1] = questions[-1][0]  # base case, start from the end

    for i in reversed(range(n - 1)):
        score, skip = questions[i]
        after = i + skip + 1
        if after < n:
            dp[i] = max(dp[i + 1], score + dp[after])  # solve current question plus the ones after skip
        else:
            dp[i] = max(dp[i + 1], score)  # if we solve this, we can't solve any questions after

    return dp[0]


print(mostPoints([[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]))
