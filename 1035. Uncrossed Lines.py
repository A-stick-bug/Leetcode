# template LCS problem, different wording

def maxUncrossedLines(nums1: list[int], nums2: list[int]) -> int:
    n, m = len(nums1), len(nums2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]
