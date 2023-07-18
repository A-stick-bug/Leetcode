from collections import Counter

def longestPalindrome(s):
    total = 0
    extra = False
    count = dict(Counter(s))
    res = {k: v for k, v in reversed(sorted(count.items(), key=lambda item: item[1]))}

    for i in res.values():
        if i % 2 == 0:
            total += i
        else:
            total += i-1
            extra = True

    if extra:
        return total + 1
    else:
        return total


s = "a"
print(longestPalindrome(s))