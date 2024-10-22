"""
https://leetcode.com/problems/check-if-dfs-strings-are-palindromes
Subtree query (euler tour) with O(1) palindrome check (hashing)
"""


from itertools import accumulate


def findAnswer(parent: list[int], s: str) -> list[bool]:
    def get_sizes(cur, prev):
        for adj in graph[cur]:
            if prev == adj:
                continue
            get_sizes(adj, cur)
            sizes[cur] += sizes[adj]

    n = len(parent)
    graph = [[] for _ in range(n)]
    for i, v in enumerate(parent):
        if i != -1 and v != -1:
            graph[i].append(v)
            graph[v].append(i)
    for i in range(n):
        graph[i].sort(reverse=True)

    sizes = [1] * n
    get_sizes(0, -1)
    inorder = []
    time = [-1] * n
    ct = 0

    def get_inorder(cur, prev):
        nonlocal ct
        inorder.append(s[cur])
        time[cur] = ct
        ct += 1
        for adj in graph[cur]:
            if adj == prev:
                continue
            get_inorder(adj, cur)

    get_inorder(0, -1)
    inorder = list(map(lambda x: ord(x) - ord("a"), inorder))

    # print(inorder)
    # print(sizes)

    # hashes
    MOD = 177635683940025046467781066894531
    p = 29
    power = [0] * n  # precompute powers of `p`, with MOD
    power[0] = 1
    for i in range(1, n):
        power[i] = (power[i - 1] * p) % MOD

    hash1 = [0] * n  # precompute hashes of each character in `inorder`
    for i in range(n):
        hash1[i] = (inorder[i] * power[n - i - 1]) % MOD
    psa1 = [0] + list(accumulate(hash1))  # psa for range hash query

    r_hash = [0] * n  # precompute hashes of reversed string
    for i in range(n):
        r_hash[i] = (inorder[n - i - 1] * power[n - i - 1]) % MOD
    psa2 = [0] + list(accumulate(r_hash))

    def is_palindrome(l, r):
        rev_l = n - r - 1
        rev_r = n - l - 1
        hash1 = (psa1[r + 1] - psa1[l]) * power[l] % MOD  # shift up
        hash2 = (psa2[rev_r + 1] - psa2[rev_l]) * power[rev_l] % MOD
        return hash1 == hash2

    ans = [False] * n
    for i in range(n):
        l = time[i]
        r = l + sizes[i] - 1
        # print(inorder[l:r+1])
        ans[i] = is_palindrome(l, r)
    return ans


print(findAnswer([-1, 2, 0, 1], "bbge"))  # ebgb
print(findAnswer(parent=[-1, 0, 0, 1, 1, 2], s="aababa"))
print(findAnswer(parent=[-1, 0, 0, 0, 0], s="aabcb"))
