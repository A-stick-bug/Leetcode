from collections import defaultdict


def maximumDetonation(bombs):
    # first turn the grid into a graph (adjacency map)
    # then do a dfs from every node and return the one that traversed most nodes
    # O(n^3) no faster solutions
    # lots of annoying edge case such as 2 bombs on the same spot (shouldn't be allowed tbh) and no bomb affects other bombs

    graph = defaultdict(list)
    dist = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2)  # euclidian distance

    def dfs(node):
        nonlocal most_detonated
        if node in visited:
            return
        visited.add(node)
        if node in graph:
            for n in graph[node]:
                dfs(n)
        return len(visited)

    # put values in graph
    i = 0
    for x1, y1, radius in bombs:
        radius **= 2
        j = 0
        for x2, y2, _ in bombs:
            if radius >= dist(x1, y1, x2, y2) and i != j:
                graph[i].append(j)
            j += 1
        i += 1
    # print(graph)

    # dfs on all nodes
    most_detonated = 0
    for node in graph.keys():
        visited = set()
        most_detonated = max(most_detonated, dfs(node))

    return 1 if graph == {} else most_detonated


bombs = [[1, 1, 5], [10, 10, 5]]
print(maximumDetonation(bombs))
