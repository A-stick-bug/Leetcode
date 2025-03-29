def reverseDegree(s: str) -> int:
    total = 0
    a = "qwertyuiopasdfghjklzxcvbnm"
    a = sorted(a)
    for i in range(len(s)):
        total += (i + 1) * (26 - a.index(s[i]))
    return total


print(reverseDegree("zaza"))
