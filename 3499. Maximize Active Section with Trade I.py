# https://leetcode.com/problems/maximize-active-section-with-trade-i
# Grouping equal elements together

def maxActiveSectionsAfterTrade(s: str) -> int:
    n = len(s)
    groups = [[int(s[0]), 1]]  # char, cnt
    for i in range(1, n):
        if s[i] == s[i - 1]:
            groups[-1][1] += 1
        else:
            groups.append([int(s[i]), 1])

    groups = [[1, 0]] + groups + [[1, 0]]

    ones = s.count("1")
    best = ones
    for i in range(1, len(groups) - 1):
        if groups[i][0] == 1 and groups[i - 1][0] == 0 == groups[i + 1][0]:
            best = max(best, ones + groups[i - 1][1] + groups[i + 1][1])
    # print(groups)
    return best


print(maxActiveSectionsAfterTrade("01"))
print(maxActiveSectionsAfterTrade("0100"))
print(maxActiveSectionsAfterTrade("1000100"))
print(maxActiveSectionsAfterTrade("01010"))
