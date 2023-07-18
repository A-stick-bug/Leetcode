def isIsomorphic(s,t):
    lookup = {}
    if len(s) != len(t):
        return False
    if not s and not t:
        return False

    for i in range(len(s)):
        if s[i] in lookup:
            if lookup[s[i]] != t[i]:
                return False
        else:
            if t[i] in lookup.values():
                return False
            else:
                lookup[s[i]] = t[i]

    return True


s = "BADC"
t = "BABA"
print(isIsomorphic(s,t))