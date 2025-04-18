# https://leetcode.com/problems/longest-palindromic-substring
# Classic string problem

# expanding 2-pointers: O(n^2), much faster on average
def longestPalindrome(s: str) -> str:
    n = len(s)
    l_ans = r_ans = 0

    for cent in range(n - 1):
        # odd case
        l = cent
        r = cent
        while 0 <= l and r < n and s[l] == s[r]:
            if r_ans - l_ans < r - l:
                l_ans = l
                r_ans = r
            l -= 1
            r += 1

        # even case
        l = cent
        r = cent + 1
        while 0 <= l and r < n and s[l] == s[r]:
            if r_ans - l_ans < r - l:
                l_ans = l
                r_ans = r
            l -= 1
            r += 1

    return s[l_ans: r_ans + 1]


print(longestPalindrome("abcbad"))


# DP solution: O(n^2)
def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # base cases: length 1 and 2
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        dp[i][i + 1] = (s[i] == s[i + 1])

    # start with smaller segments
    for le in range(3, n + 1):
        for l in range(n - le + 1):
            r = l + le - 1
            dp[l][r] = (s[l] == s[r]) and dp[l + 1][r - 1]

    # find largest valid one
    for le in reversed(range(1, n + 1)):
        for l in range(n - le + 1):
            r = l + le - 1
            if dp[l][r]:
                return s[l:r + 1]
