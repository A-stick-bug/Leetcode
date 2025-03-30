# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/
# Very cool problem, many possible approaches (here I use hashing)
# - Store all substring hashes of `t` (reversed) in a set
# - We take a palindromic substring in `s` and try to add stuff to the left
# - We can check if the stuff we add is valid by looking for the corresponding
#   strings in the `t` hashes
#
# Note: make sure 'a' doesn't become 0 when hashing or else we get collisions

MN = 2001
p = 29
mod = 1152921504606846989

power = [0] * MN
power[0] = 1
for i in range(1, MN):
    power[i] = (power[i - 1] * p) % mod


def longestPalindrome(s: str, t: str) -> int:
    def solve(s, t):
        n, m = len(s), len(t)

        # substrings of reversed `t`
        arr = [ord(i) - ord("a") + 1 for i in t][::-1]
        psa = [0] * (m + 1)
        for i in range(1, m + 1):
            psa[i] = (arr[i - 1] * power[MN - i] + psa[i - 1]) % mod
        subs = set()
        for l in range(m):
            for r in range(l, m):
                subs.add((psa[r + 1] - psa[l]) * power[l] % mod)

        # hashes of `s`
        arr = [ord(i) - ord("a") + 1 for i in s]
        psa = [0] * (n + 1)
        for i in range(1, n + 1):
            psa[i] = (arr[i - 1] * power[MN - i] + psa[i - 1]) % mod

        def query(l, r):  # query hash of [l,r]
            # shift up to match `mn`
            hs = (psa[r + 1] - psa[l]) * power[l] % mod
            return hs

        best = 0
        for cent in range(n):
            # odd case
            l = cent
            r = cent
            cur = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cur = max(cur, r - l + 1)
                l -= 1
                r += 1
            for i in range(l + 1):  # try extending left
                hs = query(i, l)
                if hs in subs:  # found match in `t`
                    cur += 2 * (l - i + 1)
                    break
            best = max(best, cur)

            # even case
            l = cent
            r = cent + 1
            cur = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cur = max(cur, r - l + 1)
                l -= 1
                r += 1
            for i in range(l + 1):  # try extending left
                hs = query(i, l)
                if hs in subs:  # found match in `t`
                    cur += 2 * (l - i + 1)
                    break
            best = max(best, cur)
        return best

    return max(solve(s, t), solve(t[::-1], s[::-1]))


print(longestPalindrome("gaj", "gtld"))  # 3
print(longestPalindrome("n", "no"))  # 2
print(longestPalindrome("a", "a"))  # 2
print(longestPalindrome("abc", "def"))  # 1
print(longestPalindrome("b", "aaaa"))  # 4
print(longestPalindrome("abcde", "ecdba"))  # 5
