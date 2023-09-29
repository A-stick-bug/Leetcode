"""
https://leetcode.com/problems/optimize-water-distribution-in-a-village/description/
Kruskal's algorithm with a virtual node to represent well
"""

from typing import List


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    # turn wells into a connection to a virtual node
    pipes.extend([[0, i + 1, val] for i, val in enumerate(wells)])
    pipes.sort(key=lambda x: x[2])

    # now we can use Kruskal's algorithm normally
    total = 0
    uf = UnionFind(n + 1)

    for a, b, cost in pipes:
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            total += cost

    return total


print(minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]))
