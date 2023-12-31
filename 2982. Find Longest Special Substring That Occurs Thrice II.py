from collections import defaultdict


def maximumLength(s: str) -> int:
    s += "{"  # extra character to ensure we don't forget about the last letters in the string
    n = len(s)
    s = list(map(lambda x: ord(x) - ord('a'), list(s)))

    scores = defaultdict(lambda: [0] * 26)  # not TLE??? when I use a N*26 list it gets TLE
    cnt = defaultdict(int)
    left = 0

    for right in range(n):  # sliding window, to find contiguous letters
        if cnt and s[right] != list(cnt.keys())[0]:
            scores[right - left][s[right - 1]] += 1
        cnt[s[right]] += 1

        while len(cnt) > 1:
            cnt[s[left]] -= 1
            if cnt[s[left]] == 0:
                del cnt[s[left]]
            left += 1

    # casework
    best = -1
    for let in range(26):
        for i in scores:
            if scores[i][let] >= 3:
                best = max(best, i)
            if scores[i][let] == 2:
                best = max(best, i - 1)
            if scores[i][let] == 1:
                best = max(best, i - 2)
                if i - 1 in scores and scores[i - 1][let] >= 1:
                    best = max(best, i - 1)

    return best if best != 0 else -1


print(maximumLength(s="aaaaa"))
