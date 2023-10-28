# find longest subsequence where all strings have equal length, hdist is 1, and are all in different groups
# handle each string length separately

from typing import List


def getWordsInLongestSubsequence(n: int, words: List[str], groups: List[int]) -> List[str]:
    def hdist(s, t):
        return sum(i != j for i, j in zip(s, t))

    wl = [[] for _ in range(11)]  # (word, index)
    for i, w in enumerate(words):
        wl[len(w)].append((w, i))

    res = []
    for length in range(1, 11):
        if not wl[length]:
            continue

        arr = wl[length]
        dp = [1] * len(arr)
        parent = [-1] * len(arr)

        for i in range(1, len(arr)):  # fill in dp table
            for j in range(i):
                if groups[arr[i][1]] != groups[arr[j][1]] and hdist(arr[i][0], arr[j][0]) == 1 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j

        trace = dp.index(max(dp))
        sub_seq = []

        while trace != -1:  # root element is guaranteed to not have parent
            sub_seq.append(wl[length][trace][1])
            trace = parent[trace]

        res.append([words[i] for i in reversed(sub_seq)])

    return max(res, key=len)


print(getWordsInLongestSubsequence(n = 5, words = ["ccb","ac","aa","bad","ab"], groups = [3,5,2,2,1]))
