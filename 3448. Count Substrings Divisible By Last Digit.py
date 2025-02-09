# https://leetcode.com/problems/count-substrings-divisible-by-last-digit
# Digit DP and modular arithmetic
# - Loop each possible ending digit separately
# - At each index equal to the ending digit, check how many previous values match
# - Transition: append digit to end, x to 10*x + s[i]

from collections import Counter


def countSubstrings(s: str) -> int:
    s = list(map(int, s))
    n = len(s)
    total = 0
    for m in range(1, 10):
        if m not in s:
            continue

        freq = Counter()

        for i in range(n):
            cur = s[i] % m

            # transition by shifting old values
            items = list(freq.items())
            freq.clear()
            for k, v in items:
                freq[(k * 10 + s[i]) % m] += v

            # add current number as starting point
            freq[cur] += 1

            if s[i] == m:
                total += freq[0]

    return total


# print(countSubstrings("1111"))
# print(countSubstrings(s="12936"))
print(countSubstrings(s="5701283"))
print(countSubstrings(s="1010101010"))
