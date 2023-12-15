# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/
# Binary lifting template, given parents of each node
# Precompute a total of log(n) ancestors for each node, so we can go up the tree by powers of 2
#
# Precompute: O(n*log(n))
# Query: O(log(n))


class TreeAncestor:
    def __init__(self, n: int, parent: list[int]):
        self.log2 = lambda x: x.bit_length() - 1
        LOG = self.log2(n) + 1

        self.table = [[-1] * LOG for _ in range(n + 1)]
        for i in range(n):
            self.table[i][0] = parent[i]

        for layer in range(1, LOG):  # compute powers of 2
            for i in range(n):  # get the parent of the parent for each node
                ancestor1 = self.table[i][layer - 1]
                ancestor2 = self.table[ancestor1][layer - 1]
                self.table[i][layer] = ancestor2

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0:
            jump = self.log2(k)
            node = self.table[node][jump]
            k -= 2 ** jump
        return node


binary_lift = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(binary_lift.getKthAncestor(3, 1))  # output 1
