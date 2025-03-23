# Difficult problem: review later
# https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal
# Trie
# For each index, we consider removing it individually
# There are only 2 possible answers, if we can't make it the max, make it the second max

from collections import defaultdict, Counter


class Trie:
    def __init__(self):
        self.count = 0  # number of times this word is stored
        self.prefix_count = 0  # number of words that can be reached from this node
        self.children = defaultdict(Trie)
        self.idx = []  # index of words stored in this node

    def insert(self, word: str, idx) -> None:
        cur = self
        cur.prefix_count += 1
        for char in word:
            cur = cur.children[char]
            cur.prefix_count += 1
        cur.count += 1
        cur.idx.append(idx)

    def get_k_nodes(self, n, k):
        res = [-1] * n

        def dfs(cur, depth, ans):
            if cur.prefix_count >= k:  # current point works as a prefix
                ans = depth
            for i in cur.idx:
                res[i] = ans
            for val in cur.children.values():
                dfs(val, depth + 1, ans)

        dfs(self, 0, 0)
        return res


def longestCommonPrefix(words: list[str], k: int) -> list[int]:
    n = len(words)
    if n == k:
        return [0] * n

    trie = Trie()
    for i in range(n):
        trie.insert(words[i], i)

    pre = trie.get_k_nodes(n, k)
    freq = Counter(pre)

    freq = sorted(freq.items(), reverse=True) + [(0, n + 1)]
    # print(freq)

    ans = [0] * n
    for i in range(n):
        # only `k` of first max, removing it makes it not enough
        # must take second max
        if pre[i] == freq[0][0] and freq[0][1] == k:
            ans[i] = freq[1][0]
        # otherwise take first max
        else:
            ans[i] = freq[0][0]
    return ans


print(longestCommonPrefix(["ccd", "adc", "dba", "bff", "cbfae", "fcae", "cbbc"], 3))
print(longestCommonPrefix(words=["juaa", "run", "run", "juaa", "run"], k=2))
print(longestCommonPrefix(words=["dog", "racer", "car"], k=2))
