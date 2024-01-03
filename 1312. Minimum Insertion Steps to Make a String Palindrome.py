# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# we observe that the number of character we need to insert is just (length of s) - (longest palindromic subsequence)

def minInsertions(s: str) -> int:
    def longestPalindromeSubseq_iterative(s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # 1 letter is always a palindrome

        for i in range(n):  # base case: single letters are always palindromes
            dp[i][i] = 1

        # fill up the rest of the table using bases cases
        for i in reversed(range(n - 1)):  # iterate in reversed since we are accessing [i+1]
            for j in range(i + 1, n):  # iterate normally since we are accessing [j-1]
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2  # add 2 letters to interval
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # skip a letter
        return dp[0][n - 1]

    return len(s) - longestPalindromeSubseq_iterative(s)


print(minInsertions("leetcode"))
