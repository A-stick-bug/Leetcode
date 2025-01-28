# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/
# Tricky tree DP
# Maximum the sum at the end means minimize the removed sum

def maximizeSumOfWeights(edges: list[list[int]], k: int) -> int:
    inf = 1 << 60
    n = len(edges) + 1
    graph = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def compute_cost(arr, k):
        # we can take at most `k` from `a`
        # greedily minimize cost, we take the `a` with the biggest difference compared to `b`
        arr.sort(key=lambda x: x[1] - x[0], reverse=True)
        return sum(a for a, b in arr[:k]) + sum(b for a, b in arr[k:])

    def solve(cur, prev):
        if len(graph[cur]) == 1 and cur != 0:  # base case: leaf
            return 0, graph[cur][0][1]

        options = []
        par_val = inf  # cost to remove edge to parent node
        for adj, val in graph[cur]:
            if adj == prev:
                par_val = val
                continue
            c1, c2 = solve(adj, cur)
            options.append((c1, c2))

        # calculate cheapest if we keep the parent edge
        if cur == 0:
            # at root, no parent edge to consider
            cost1 = compute_cost(options, k)
        else:
            # any other node, `k-1` to keep parent edge
            cost1 = compute_cost(options, k - 1)

        # calculate cheapest with parent edge removed
        cost2 = par_val + compute_cost(options, k)

        # return (overall cheapest, cheapest if we remove the parent edge)
        return min(cost1, cost2), cost2

    return sum(i for _, _, i in edges) - solve(0, -1)[0]


print(maximizeSumOfWeights(edges=[[0, 1, 4], [0, 2, 2], [2, 3, 12], [2, 4, 6]], k=2))  # 22
print(maximizeSumOfWeights(edges=[[0, 1, 5], [1, 2, 10], [0, 3, 15], [3, 4, 20], [3, 5, 5], [0, 6, 10]], k=3))  # 65

print(maximizeSumOfWeights([[0, 1, 25], [0, 2, 10], [1, 3, 29]], 1))  # 39
print(maximizeSumOfWeights([[0, 1, 34], [0, 2, 17]], 1))  # 34
