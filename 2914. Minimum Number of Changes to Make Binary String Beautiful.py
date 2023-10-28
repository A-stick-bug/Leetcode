# using not to switch between odd and even

def minChanges(s: str) -> int:
    groups = []  # odd/even
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count = not count
        else:
            groups.append(count)
            count = 1
    if count:
        groups.append(count)  # trailing group

    res = 0
    for i in range(len(groups) - 1):
        if groups[i] == 1:
            groups[i] = 0
            groups[i + 1] = not groups[i + 1]
            res += 1
    return res


print(minChanges("01010000011001001101"))
