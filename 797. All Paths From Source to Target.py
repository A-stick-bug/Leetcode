def allPathsSourceTarget(graph):
    end = len(graph) - 1
    paths = []
    stack = [[0]]

    while stack:
        path = stack.pop()
        node = path[-1]
        if node == end:
            paths.append(path)
            continue
        for adj in graph[node]:
            stack.append(path+[adj])

    return paths
