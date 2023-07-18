def numKLenSubstrNoRepeats(s: str, k: int) -> int:
    """
    :param s: string to use sliding window on
    :param k: length of window
    :return: amount of windows with length k without duplicate characters
    """
    res = start = 0
    window = set()
    for end in range(len(s)):
        while s[end] in window:
            window.remove(s[start])
            start += 1

        window.add(s[end])
        if end - start + 1 == k:
            res += 1
