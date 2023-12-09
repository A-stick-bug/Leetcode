def removeAlmostEqualCharacters(word: str) -> int:
    c = 0
    i = 1
    while i < len(word):
        if abs(ord(word[i]) - ord(word[i-1])) <= 1:
            c += 1
            i += 1
        i += 1
    return c


print(removeAlmostEqualCharacters("aaaaa"))
