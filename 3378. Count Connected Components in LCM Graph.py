# https://leetcode.com/problems/count-connected-components-in-lcm-graph
# When only connectivity matters and the number of edges are too high, consider
# using a disjoint set and only connecting necessary edges
#
# - first filter numbers >threshold since the LCM of 2 numbers is at least their maximum
# - loop through all possible divisors <=threshold as the GCD and calculate LCM based on this
# - lcm(a,b) = a*b/gcd(a,b)

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


def countComponents(nums: list[int], threshold: int) -> int:
    original_n = len(nums)
    nums = [i for i in nums if i <= threshold]
    nums = set(nums)
    n = len(nums)

    ds = DisjointSet(threshold + 1)

    for div in range(1, threshold + 1):  # loop divisors
        res = []
        for mul in range(div, threshold + 1, div):  # loop multiples of divisors
            if mul in nums:
                res.append(mul)
        for i in range(1, len(res)):  # join divisors if LCM < threshold
            if res[0] * res[i] <= threshold * div:
                ds.union(res[0], res[i])
            else:  # exceeded threshold, break since res is ascending
                break

    # count components and single nodes that were filtered out
    return sum(ds.find(i) == i for i in nums) + (original_n - n)


print(countComponents(nums=[2, 4, 8, 3, 9], threshold=5))
print(countComponents(nums=[2, 4, 8, 3, 9, 12], threshold=10))
