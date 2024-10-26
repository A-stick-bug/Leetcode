# https://leetcode.com/problems/find-subtree-sizes-after-changes/description/
# first get the closest parent with same value using dfs
# then get subtree sizes with tree dp

def findSubtreeSizes(parent: list[int], s: str) -> list[int]:
    n = len(parent)
    graph = [[] for _ in range(n)]
    for i, v in enumerate(parent):
        if i != -1 and v != -1:
            graph[i].append(v)
            graph[v].append(i)

    new_par = [-1] * n

    def solve(cur, prev, letters):
        letters[ord(s[cur]) - ord('a')] = cur  # closest parent with letter x
        for adj in graph[cur]:
            if adj == prev:
                continue
            c = ord(s[adj]) - ord('a')
            if letters[c] != -1:
                new_par[adj] = letters[c]
            else:
                new_par[adj] = cur
            solve(adj, cur, letters.copy())

    solve(0, -1, [-1] * 26)

    graph2 = [[] for _ in range(n)]
    for i, v in enumerate(new_par):
        if i != -1 and v != -1:
            graph2[i].append(v)
            graph2[v].append(i)

    sizes = [1] * n

    def get_sizes(cur, prev):
        for adj in graph2[cur]:
            if adj == prev:
                continue
            get_sizes(adj, cur)
            sizes[cur] += sizes[adj]

    get_sizes(0, -1)
    return sizes


print(findSubtreeSizes(parent=[-1, 0, 0, 1, 1, 1], s="abaabc"))
print(findSubtreeSizes(parent=[-1, 0, 4, 0, 1], s="abbba"))
