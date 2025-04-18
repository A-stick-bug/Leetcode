# https://leetcode.com/problems/shortest-palindrome/
# Problem simplifies to finding the longest prefix that is a palindrome
# As usual, we could use hashing
# Here, I use the Z-algorithm as it has a better constant factor
#
#
# TC: O(n)

def shortestPalindrome(s: str) -> str:
    if s == s[::-1]:  # entirely palindrome
        return s

    n = len(s)

    def z_algorithm(s):
        n = len(s)
        z = [0] * n
        l = r = 0
        for i in range(1, n):
            if l <= i <= r:
                if i + z[i - l] - 1 < r:
                    z[i] = z[i - l]
                else:
                    z[i] = r - i + 1
                    l = i
                    for j in range(r + 1, n):
                        if s[j - i] == s[j]:
                            z[i] += 1
                            r = j
                        else:
                            break
            else:
                l = i
                for j in range(i, n):
                    if s[j - i] == s[j]:
                        z[i] += 1
                        r = j
                    else:
                        break
        return z

    # match prefix of s in the reverse string
    matching = s + "!" + s[::-1]

    z = z_algorithm(matching)
    for i in range(n + 1, 2 * n + 1):
        # match extends to the end of reversed string, so it's a prefix palindrome
        if i + z[i] == 2 * n + 1:
            s_idx = i - (n + 1)
            return s[-s_idx:][::-1] + s


print(shortestPalindrome("a"))
print(shortestPalindrome("abac"))
