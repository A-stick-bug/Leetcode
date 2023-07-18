from collections import defaultdict

def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    indices = defaultdict(int)
    start = end = 0
    res = 0

    while end < len(s):
        indices[s[end]] = end
        if len(indices) > k:  # more than k distinct characters
            delete = min(indices.values())  # get the minimum index
            start = delete + 1
            indices.pop(s[delete])  # remove the element that has the minimum index
        res = max(res, end-start+1)
        end += 1

    return res


s = "eceba"; k = 2
print(lengthOfLongestSubstringKDistinct(s,k))
