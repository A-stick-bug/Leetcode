def findValidPair(s: str) -> str:
    for i in range(1, len(s)):
        if s[i] != s[i - 1] and s.count(s[i]) == int(s[i]) and s.count(s[i - 1]) == int(s[i - 1]):
            return s[i - 1] + s[i]
    return ""


print(findValidPair("2523533"))
print(findValidPair("221"))
print(findValidPair("22"))
