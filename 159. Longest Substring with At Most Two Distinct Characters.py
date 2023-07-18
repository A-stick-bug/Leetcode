from collections import defaultdict


def longest_distinct(s):
    start = end = 0
    window = defaultdict(int)
    res = 0
    while end < len(s):
        window[s[end]] = end  # keep track of most recent index of this character
        end += 1
        if len(window) > 2:
            # move the window's start until there is less than 2 distinct characters
            delete = min(window.values())
            window.pop(s[delete])
            start = delete + 1
        res = max(res, end - start + 1)  # check if current window length if longer

    return res


print(longest_distinct("ccaabbb"))
