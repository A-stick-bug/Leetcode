def isOneEditDistance(s: str, t: str) -> bool:
    # 2 pointers solution
    # check is one string can be turned into the other by deleting, inserting, or changing one letter
    # note: inserting is the same as deleting from the other string so we only consider deleting

    ls, lt = len(s), len(t)
    if abs(ls - lt) > 1:
        return False

    if ls > lt:  # s should be shorter than t for the comparison
        # return self.isOneEditDistance(t, s)
        return isOneEditDistance(t, s)

    diff = 0
    start = end = 0
    while end < lt and start < ls:
        if s[start] != t[end]:
            if ls != lt:  # t is longer than s
                end += 1
            else:
                start += 1
                end += 1
            diff += 1
        else:
            start += 1
            end += 1

    # 2 strings are the same or difference is more than 1
    if (diff == 0 and ls == lt) or diff > 1:
        return False
    return True


s = "a"; t = "ac"
print(isOneEditDistance(s,t))
