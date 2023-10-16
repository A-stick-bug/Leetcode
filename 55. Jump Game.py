# 3 solutions O(n), O(n*log(n)), O(n^2)


# optimal solution using greedy, going backwards, O(n)
def greedy(nums: list[int]):
    n = len(nums)
    last = n - 1  # right-most index that can be reached
    for i in reversed(range(n - 1)):
        if i + nums[i] >= last:  # can reach earlier index
            last = i
    return last == 0  # can get from end to start


# Solution 2 using Fenwick Tree O(n*log(n))
class FenwickTree:  # 1-indexed, supports range update and point query
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        i += 1
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def range_add(self, l, r, val):
        self.add(l, val)
        self.add(r + 1, -val)

    def query(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret


# Index 0 is always reachable (base case)
# Loop through every index (except last) and if the current index is reachable:
#    We can reach the next nums[i] indices from i, so we set those to true (this is optimized with Fenwick Tree)
def canJump(nums: list[int]) -> bool:
    n = len(nums)
    reachable = FenwickTree(n)
    reachable.range_add(0, 0, 1)  # base case: index 0 is always reachable

    for i in range(n - 1):
        if reachable.query(i):  # if the current index is reachable
            if i + nums[i] + 1 >= n:  # optimization: return early if we can reach end
                return True
            reachable.range_add(i + 1, min(i + nums[i], n - 1), 1)  # we can also reach the next nums[i] indices

    return reachable.query(n - 1) > 0  # return whether we can reach the last index


# TLE, Solution 3 using brute force O(n^2)
def brute_force(nums: list[int]) -> bool:
    n = len(nums)
    reachable = [False] * n
    reachable[0] = True

    for i in range(n - 1):
        if reachable[i]:  # range updating like this is too slow
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                reachable[j] = True

    return reachable[-1]
