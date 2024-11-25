# anagram check on chunks of the string

def isPossibleToRearrange(s: str, t: str, k: int) -> bool:
    n = len(s)
    le = n // k

    subs = [s[i:i + le] for i in range(0, n, le)]
    subs2 = [t[i:i + le] for i in range(0, n, le)]
    return sorted(subs) == sorted(subs2)


print(isPossibleToRearrange(s="aabbcc", t="bbaacc", k=3))
