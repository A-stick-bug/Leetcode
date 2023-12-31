def maximumLength(s: str) -> int:
    def cnt(sub):
        c = 0
        for i in range(n):
            if s[i:].startswith(sub):
                c += 1
        return c

    n = len(s)

    best = -1
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if len(set(sub)) == 1:
                cur = cnt(sub)
                if cur >= 3:
                    best = max(best, len(sub))

    return best


print(maximumLength( s = "abcaba"))
