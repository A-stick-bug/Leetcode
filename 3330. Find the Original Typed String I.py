# simple implementation

def possibleStringCount(word: str) -> int:
    group = [1]
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            group[-1] += 1
        else:
            group.append(1)

    return sum(i - 1 for i in group) + 1


print(possibleStringCount("aaa"))
