# https://leetcode.com/problems/incremental-even-weighted-cycle-queries/description/
# Augment a disjoint set to use it as a dynamic tree structure
#
# Main observation:
# - when adding a new edge, if we are connecting 2 disjoint components,
#   we can obviously add it
# - otherwise, we can add it if the current path's parity doesn't conflict
#   - notice how we don't need to check every cycle
#
# Now the problem becomes support dynamic tree operations:
# - query mod 2 distance between 2 nodes
# - join 2 nodes together
#
# The disjoint set supports the join feature, so we will base our structure on it
# To track distances, we need to augment, add mod 2 distance to the root
# - this allows us to get the distance between any 2 nodes in the component
# - the idea is from LCA: dist(a,b) = dist(a,root) + dist(b, root) - 2dist(lca, root)
#   - here the 2dist(lca, root) is always even (thus 0) so it can be ignored
#   - thus we don't even need to track the lca
# We also need to track the nodes in each component
# When merging, recompute the smaller component's nodes only
#
# TC: O(n log n), by small to large merging
#
# note: apparently, you can get O(n) by updating distances lazily
#       inside of the `.find` function

class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
        # augmentations
        self.dist = [0] * N  # distance to root mod 2
        self.sub = [[i] for i in range(N)]  # entire subtree

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b, c):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
            a, b = b, a

        # join b to a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]

        a_to_r = self.dist[a]
        upd = []
        for s in self.sub[root_b]:
            # update distances from smaller component: distance is now to the root of a
            upd.append((a_to_r ^ c) ^ (self.dist[s] ^ self.dist[b]))
        for s, u in zip(self.sub[root_b], upd):
            self.dist[s] = u
        self.sub[root_a].extend(self.sub[root_b])


def numberOfEdgesAdded(n: int, edges: list[list[int]]) -> int:
    total = 0
    ds = DisjointSet(n)
    for a, b, c in edges:
        if ds.find(a) != ds.find(b):  # union here
            ds.union(a, b, c)
            total += 1
        else:  # xor dist
            d = ds.dist[a] ^ ds.dist[b] ^ c
            if d == 0:  # no contradiction
                total += 1
    return total
