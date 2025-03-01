# https://leetcode.com/problems/select-k-disjoint-special-substrings
# Tarjan's algorithm for SCC
# Construct the following graph:
# - graph[x] = letters covered by [first x, last x]
#
# Compress SCCs to get a DAG and taking leaves guarantees that you take the maximum amount of nodes
# Corner case:
# - K = 1, valid if there are at least 2 nodes in SCC graph (if there's only 1, that's the whole string)

from collections import defaultdict
import sys
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(200000)


def maxSubstringLength(s: str, K: int) -> bool:
    s = "{" + s + "{"  # `{` will be the root of the constructed graph
    if K == 0:
        return True

    def get_scc(graph):
        n = len(graph)

        scc = [-1] * n  # the component that node i belongs to
        comp = 1  # current component
        low_link = [-1] * n  # smallest time reachable of a node reachable from the DFS subtree of node i
        node_id = [-1] * n  # time at which node i was discovered
        time = 0
        path = []  # nodes currently in the dfs traversal
        in_path = [False] * n

        def dfs(cur):
            nonlocal time, comp
            node_id[cur] = low_link[cur] = time
            path.append(cur)
            in_path[cur] = True
            time += 1

            for adj in graph[cur]:
                if node_id[adj] == -1:  # not yet visited
                    dfs(adj)
                    low_link[cur] = min(low_link[cur], low_link[adj])

                elif in_path[adj]:  # back edge, since we arrived at a node on the current path
                    low_link[cur] = min(low_link[cur], node_id[adj])

                else:
                    # 1-way path to another component, NOT back edge
                    continue

            if node_id[cur] == low_link[cur]:  # root in dfs tree, assign SCC values to everything in this SCC
                while True:
                    in_path[path[-1]] = False
                    scc[path[-1]] = comp
                    if path.pop() == cur:
                        break
                comp += 1

        for i in range(n):
            if node_id[i] == -1:
                dfs(i)
        return scc

    def compress_graph(graph):
        """compress each SCC of a graph into a single node"""
        scc = get_scc(graph)
        compressed = [set() for _ in range(max(scc) + 1)]
        for i in range(len(graph)):
            for adj in graph[i]:
                if scc[i] != scc[adj]:
                    compressed[scc[i]].add(scc[adj])
        return list(map(list, compressed))  # save memory by converting back to list

    n = len(s)

    locs = defaultdict(list)  # index occurrences of each character
    for i, v in enumerate(s):
        locs[ord(v) - ord("a")].append(i)

    graph = [[] for _ in range(27)]  # taking x forces you to take all oh graph[x]
    for k in locs:
        for l in locs:
            if k == l:
                continue
            start, end = locs[k][0], locs[k][-1]
            # check if taking k forces you to take l
            if bisect_right(locs[l], end) - bisect_left(locs[l], start) > 0:
                graph[k].append(l)

    graph = compress_graph(graph)
    nodes = set()  # all nodes excluding the root
    for i in graph:
        nodes.update(i)
    # print(graph)

    leaves = [i for i in nodes if (len(graph[i]) == 0)]

    if K == 1:  # special case: not allowed to take entire string
        return len(nodes) > 1  # must be at least 2 others nodes other than the root
    return len(leaves) >= K


print(maxSubstringLength("awqbfnikfyzseidnttitakhofkzeqqnegixcndrsrelyiarmoyphbscfwjqxomjqlucqmubypcfdoxlm", 1))
print(maxSubstringLength(
    "nbuirvanjiccnsyyyoirleqsrwrvxepaglcidqplyryujytzqoncxjgwdmatytgwhzyhlsodrbzrpbbitovtdasazjtoyyfhowqqrzuvjveydceouscrfazzoblqhalhfybwheybkpcroijxvarrtqrqnmwslkpdducfeblvfecyjyulxgahxlzlyztssfzwvfujrriryslkvdwhmkcyebfhkadrahunvxivkwitilyzknwyujtylahgmlddymlbrbrniomepbmdieasuvdcqnzfwspxewbbpruxrznjxwnjjxvblxyrgv",
    1))
print(maxSubstringLength("apqd", 1))
print(maxSubstringLength(s="abcdbaefghghfab", K=2))
print(maxSubstringLength(s="cdefdc", K=3))  # 0
print(maxSubstringLength(s="abeabe", K=0))
