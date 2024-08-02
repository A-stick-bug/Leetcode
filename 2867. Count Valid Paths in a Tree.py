# https://leetcode.com/problems/count-valid-paths-in-a-tree/
# All-paths tree DP, join subtree path pairs at each node and pass information up the tree
# At each node, we store: # of subtree paths with (0 primes, 1 prime)
# TC: O(n) or O(X*log(log(X)), tree dp TC or sieving TC


def countPaths(n: int, edges: list[list[int]]) -> int:
    # precompute primes using sieve
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, n + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

    # create graph
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    total = 0

    def solve(cur, prev):
        nonlocal total
        if len(graph[cur]) == 1 and cur != 1:  # leaf node
            if is_prime[cur]:
                return [0, 1]
            else:
                return [1, 0]

        match = [0, 0]  # joined children answers
        for adj in graph[cur]:
            if adj == prev:
                continue
            child = solve(adj, cur)
            # match child branches
            if is_prime[cur]:
                total += child[0] + (child[0] * match[0])
            else:
                total += ((match[0] + 1) * child[1]) + (match[1] * child[0])

            match[0] += child[0]  # add current branch as matching option
            match[1] += child[1]

        # 0 -> 1, 1 -> 2 (we don't care about path with >1 prime)
        if is_prime[cur]:
            return [0, 1 + match[0]]
        else:
            match[0] += 1
            return match

    solve(1, -1)
    return total


print(countPaths(n=5, edges=[[1, 2], [1, 3], [2, 4], [2, 5]]))
print(countPaths(n=6, edges=[[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]]))
