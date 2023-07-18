# know when to use for/while loops, for this question, while loop is much better
# try to make code not break on edge cases
# use while loop to keep 2 pointers in range

def longestPalindrome(s: str) -> str:
    longest = 1
    out = s[0]
    for i in range(len(s)):  # for every index (and pair of indices)

        start = end = i  # center is one element
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > longest:
                out = s[start:end + 1]
                longest = end - start + 1
            start -= 1
            end += 1

        start, end = i, i + 1  # center is 2 elements
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > longest:
                out = s[start:end + 1]
                longest = end - start + 1
            start -= 1
            end += 1
    return out


def dp_solution(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    res = s[0]  # placeholder in case there is no longer palindrome

    for i in range(n):  # any single letter is a palindrome
        dp[i][i] = True

    for j in range(n):
        for i in range(j):
            if s[i] == s[j] and (dp[i + 1][j - 1] or j == i + 1):
                dp[i][j] = True
                if j - i + 1 > len(res):  # longer than current longest
                    res = s[i:j + 1]
    return res

s = "a"
print(longestPalindrome(s))
