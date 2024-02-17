# observation: the most frequently occurring letters will stay until the last removal
# to output then in order, we iterate in reverse since we remove from the left first

from collections import Counter

def lastNonEmptyString(s: str) -> str:
    freq = Counter(s).most_common()
    most = freq[0][1]
    res = set()
    for i in range(len(freq)):
        if freq[i][1] == most:
            res.add(freq[i][0])

    letters = []
    for i in reversed(s):
        if i in res and i not in letters:
            letters.append(i)
    return "".join(reversed(letters))


print(lastNonEmptyString(s = "abcd"))

