# https://leetcode.com/problems/find-the-count-of-good-integers
# There are only 2*10^5 palindromic integers less than 10^10
# Just loop through all length n palindromes and check if there is an arrangement divisible by K
# We use the lex-min (sorted) version of a number to represent the default arrangement

from collections import Counter
from math import comb

# precompute palindrome numbers and group by length
palindromes = set()
for i in range(1, 10 ** 5):
    s_i = str(i)
    rev = s_i[::-1]
    p_i1 = s_i + rev[1:]
    p_i2 = s_i + rev
    palindromes.add(p_i1)
    palindromes.add(p_i2)
palindromes = sorted(palindromes)

length_p = [[] for _ in range(11)]
for p in palindromes:
    length_p[len(p)].append(p)


def countGoodIntegers(n: int, k: int) -> int:
    def perm_without_duplicates_no_leading_zero(s):
        """Count the number of UNIQUE permutations of a string of digits `s`
        that don't have leading zeros"""
        places = len(s)
        freq = Counter(s)
        total = 1
        for i in range(10):
            if i == 0:  # 0 can't be at the start
                total *= comb(places - 1, freq[str(i)])
            else:
                total *= comb(places, freq[str(i)])
            places -= freq[str(i)]
        return total

    # loop over length n palindromes to store good arrangements
    total = 0
    vis = set()
    for p in length_p[n]:
        if int(p) % k == 0 and "".join(sorted(p)) not in vis:
            total += perm_without_duplicates_no_leading_zero(p)
            vis.add("".join(sorted(p)))
    return total


print(countGoodIntegers(n=3, k=5))
print(countGoodIntegers(n=1, k=4))
print(countGoodIntegers(n=5, k=6))
