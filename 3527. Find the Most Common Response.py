# https://leetcode.com/problems/find-the-most-common-response/description/
# just implement it, a set can be used to remove duplicates and a map can be used to count the number of occurrences

from collections import Counter


def findCommonResponse(responses: list[list[str]]) -> str:
    arr = [list(set(i)) for i in responses]
    res = []
    for i in arr:
        res.extend(i)

    freq = Counter(res)
    vals = list(freq.items())
    vals.sort(key=lambda x: (-x[1], x[0]))
    return vals[0][0]
