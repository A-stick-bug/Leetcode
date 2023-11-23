# TIME LIMIT EXCEEDED
# tried optimizing with fenwick tree for fast range query but still too slow

class FenwickTree:  # uses 1-indexing
    def __init__(self, size: int):
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: float) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total

    def range_sum(self, left, right):
        if left > right:
            return 0
        return self.query(right) - self.query(left - 1)


def new21Game(n: int, k: int, maxPts: int) -> float:
    p = 1 / maxPts
    dp = [0] * (n + 1)
    dp[0] = 1  # before the game starts, you will always have 0 points
    bit = FenwickTree(n + 1)
    bit.update(1, 1)  # update first element to match dp

    for i in range(1, n + 1):
        total = bit.range_sum(max(0, i - maxPts) + 1, min(i, k))
        dp[i] += p * total
        bit.update(i + 1, p * total)

    print(dp)
    return bit.range_sum(k+1, n+1)


print(new21Game(n=21, k=17, maxPts=10))
