# sliding window, slow but simple code
from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    start = 0
    end = len(s1) - 1

    while end < len(s2):
        if Counter(s1) == Counter(s2[start:end+1]):
            return True
        else:
            start += 1
            end += 1

    return False


s1 = "adc"
s2 = "dcda"
print(checkInclusion(s1, s2))
