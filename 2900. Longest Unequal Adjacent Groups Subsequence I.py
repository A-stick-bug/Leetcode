# basically find the longest alternating subsequence of 0 and 1
# this can be done with greedy

from typing import List


def getWordsInLongestSubsequence(n: int, words: List[str], groups: List[int]) -> List[str]:
    res = [0]

    prev = groups[0]
    for i, num in enumerate(groups):
        if num != prev:
            prev = num
            res.append(i)

    return [words[i] for i in res]


print(getWordsInLongestSubsequence(n=4, words=["a", "b", "c", "d"], groups=[1, 0, 1, 1]))
