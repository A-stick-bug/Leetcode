# https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters
# Lex min -> greedily build character by character, try to use smallest character
# We know that we can put a character if we can still complete the rest of the string
# TC: O(n * 26^2), much faster in practice due to skipping indices

def lexSmallestAfterDeletion(s: str) -> str:
    n = len(s)
    s = [ord(i) - ord("a") for i in s]
    ans = []
    unused = set(s)

    loc = [[] for _ in range(26)]
    for i, v in enumerate(s):
        loc[v].append(i)
    for c in range(26):
        loc[c].reverse()

    i = 0
    while i < n:
        if not unused:  # no more characters needed
            return "".join([chr(c + ord("a")) for c in ans])

        for c in range(26):
            while loc[c] and loc[c][-1] < i:
                loc[c].pop()
        for c in range(26):
            if loc[c]:
                first_c = loc[c][-1]
                if c in unused and first_c == i:  # forced
                    ans.append(c)
                    unused.discard(c)
                    i = first_c + 1
                    break

                if all(loc[x] and loc[x][0] >= first_c for x in unused):
                    ans.append(c)
                    unused.discard(c)
                    i = first_c + 1
                    break
    return "".join([chr(c + ord("a")) for c in ans])


print(lexSmallestAfterDeletion("aaccb"))