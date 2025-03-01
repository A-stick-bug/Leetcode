def hasSpecialSubstring(s: str, k: int) -> bool:
    for i in range(len(s) - k + 1):
        sub = s[i:i + k]

        if len(set(sub)) == 1:
            c = sub[0]
            if (i == 0 or s[i - 1] != c) and (i == len(s) - 1 or s[i + 1] != c):
                return True
    return False
