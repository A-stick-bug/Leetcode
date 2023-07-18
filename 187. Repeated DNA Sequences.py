# using "if value in set" is faster than "if value in list"

def findRepeatedDnaSequences(s: str):
    once = set()
    twice = set()
    for i in range(len(s)-9):
        sub = s[i:i + 10]
        if sub not in once:
            once.add(sub)
        elif sub not in twice:
            twice.add(sub)

    return list(twice)


s = "AAAAAAAAAAA"
print(findRepeatedDnaSequences(s))
