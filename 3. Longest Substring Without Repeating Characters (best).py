def lengthOfLongestSubstring(s: str) -> int:
    table = {}  # keeps track of the index of where a character was last seen
    start = 0
    res = 0

    for end in range(len(s)):
        if s[end] in table.keys():  # character is already in window
            start = max(start, table[s[end]] + 1)

        res = max(res, end - start + 1)
        table[s[end]] = end
    return res


print(lengthOfLongestSubstring("abba"))
