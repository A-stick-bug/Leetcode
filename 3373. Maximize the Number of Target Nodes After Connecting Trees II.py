# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
# Key observation:
# - First consider tree rerooting DP
#   - as you go to an adjacent node, the number of even and odd paths to other nodes swap
# - that is, odd paths become even and even paths become odd
# - When connecting to the second graph, we want to maximize the odd paths

def maxTargetNodes(edges1, edges2):
    n = len(edges1) + 1
    graph1 = [[] for _ in range(n)]  # create graphs
    for a, b in edges1:
        graph1[a].append(b)
        graph1[b].append(a)
    m = len(edges2) + 1
    graph2 = [[] for _ in range(m)]
    for a, b in edges2:
        graph2[a].append(b)
        graph2[b].append(a)

    def get_parities(graph, start):
        """2 color the tree, where res[i] is the color of node i"""
        n = len(graph)
        res = [-1] * n
        stack = [(start, -1, 0)]
        while stack:
            cur, prev, d = stack.pop()
            res[cur] = d % 2
            for adj in graph[cur]:
                if adj == prev:
                    continue
                stack.append((adj, cur, d + 1))
        return res

    par1 = get_parities(graph1, 0)
    par2 = get_parities(graph2, 0)

    graph2_odd = max(par2.count(0), par2.count(1))  # max odd length in graph2

    graph1_par = [par1.count(0), par1.count(1)]
    res = []
    for i in range(n):
        # odd and even paths swap depending on color of node
        # if the node is color 0, the path to all other color 0 nodes has even length
        res.append(graph1_par[par1[i]] + graph2_odd)

    return res


print(maxTargetNodes(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                     edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]))
print(maxTargetNodes(edges1=[[0, 1], [0, 2], [0, 3], [0, 4]], edges2=[[0, 1], [1, 2], [2, 3]]))
