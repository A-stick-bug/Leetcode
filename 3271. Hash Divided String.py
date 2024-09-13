# https://leetcode.com/problems/hash-divided-string
# just implement it

def stringHash(s: str, k: int) -> str:
    n = len(s)
    block = n // k
    zero = ord('a')

    res = []
    for i in range(block):
        sub = s[i * k: (i + 1) * k]
        res.append(chr(zero + sum(ord(i) - zero for i in sub) % 26))

    return "".join(res)


print(stringHash(s="mxz", k=3))
