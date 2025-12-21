# https://leetcode.com/problems/max-points-on-a-line
# Might've overkilled a bit
# Group by slopes and use a disjoint set to get which points are on the same line
# TC: O(n^2)
#
# Easier alternate solution: For each point, consider which slope it makes with the max amount of other points

from collections import defaultdict
from math import gcd


class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


def maxPoints(points: list[list[int]]) -> int:
    def get_slope(a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        g = gcd(dx, dy)  # avoid floating points
        return dx // g, dy // g

    n = len(points)
    slopes = defaultdict(list)

    for i in range(n):  # group pairs of points by slope between them
        for j in range(i + 1, n):
            slope = get_slope(points[i], points[j])
            slopes[slope].append((i, j))

    ds = DisjointSet(n)
    mx_size = 0
    for group in slopes.values():  # for each slope, get the biggest group of parallel points
        points = set()  # points in this group
        for a, b in group:
            points.add(a)
            points.add(b)
            ds.union(a, b)
        roots = {ds.find(i) for i in points}
        sz = max(ds.size[root] for root in roots)
        mx_size = max(mx_size, sz)

        # reset disjoint set
        for i in points:
            ds.parent[i] = i
            ds.size[i] = 1

    return mx_size


print(maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
