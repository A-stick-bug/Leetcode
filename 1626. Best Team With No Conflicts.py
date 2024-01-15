# https://leetcode.com/problems/best-team-with-no-conflicts/description/
# First sort by age, now we just need to find the longest non-decreasing subsequence
# Note: we are also sorting by score so people with same age are in increasing order of score
# O(n*log(n)) using Fenwick Tree

class MaxFenwickTree:  # uses 1-indexing
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, val: int) -> None:
        """Set self.bit[i] to val"""
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total = max(total, self.bit[i])
            i -= i & (-i)
        return total


def bestTeamScore(scores: list[int], ages: list[int]) -> int:
    people = list(zip(ages, scores))  # people[i][0] is age, [1] is score
    people.sort(key=lambda x: (x[0], x[1]))  # sort by age and score

    ordered = sorted(set(scores))  # coordinate compression on scores
    compress = {ordered[i]: i + 1 for i in range(len(ordered))}

    bit = MaxFenwickTree(len(ordered))
    for _, score in people:  # find LIS of scores
        rank = compress[score]
        best = bit.query(rank)  # equal elements allowed
        bit.update(rank, best + score)  # adding the current player gives extra score

    return bit.query(len(ordered))  # return sequence with max scores
