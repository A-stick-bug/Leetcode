# Tricky question
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# strategy: group adjacent substrings together to use sliding window
# we can use a Counter() to check for matching in O(1)
#
# TC: O(NW), where W is a single word's length

from collections import Counter


def findSubstring(s: str, words: list[str]) -> list[int]:
    res = []
    M = len(words)
    W = len(words[0])
    match_words = Counter(words)

    # different starting indices to cover all possible substrings of length W
    # while grouping adjacent ones together
    for start in range(W):
        cur = s[start:]
        freq = Counter(words)  # words that still need to be matched, empty when fully matched
        chunks = [cur[i * W: (i + 1) * W] for i in range(len(cur) // W)]
        # print(chunks)
        extras = Counter()  # words in the window but not currently used in matching

        for r in range(len(chunks)):  # sliding window
            l = r - M + 1
            if chunks[r] in freq:  # shift window right, add word
                freq[chunks[r]] -= 1
                if freq[chunks[r]] == 0:
                    del freq[chunks[r]]
            elif chunks[r] in match_words:
                extras[chunks[r]] += 1

            if not freq:  # fully matched, add index
                res.append(start + l * W)

            if l >= 0 and chunks[l] in match_words:  # shift window left if needed, remove word
                if extras[chunks[l]] > 0:
                    extras[chunks[l]] -= 1
                else:
                    freq[chunks[l]] += 1

    return res


print(findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
print(findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
print(findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
print(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
