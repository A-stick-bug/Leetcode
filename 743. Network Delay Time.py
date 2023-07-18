from collections import defaultdict
import heapq


def networkDelayTime(times, n, k):
    """
    :param times: adjacency list of the graph
    :param n: number of nodes
    :param k: starting node
    :return: minimum time for all nodes to recieve signal, -1 if a node is not connected
    """
    # create the graph
    graph = defaultdict(list)
    for node1, node2, time in times:
        graph[node1].append((time, node2))

    visited = set()
    q = [(0, k)]
    while q:
        time, node = heapq.heappop(q)
        visited.add(node)

        # check is all nodes have been visited
        if len(visited) == n:
            return time

        for t, adj_node in graph[node]:
            if adj_node not in visited:
                heapq.heappush(q, (time + t, adj_node))
    return -1


times = [[2,1,1],[2,3,1],[3,4,1]]; n = 4; k = 2
print(networkDelayTime(times,n,k))
