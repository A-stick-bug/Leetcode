# https://leetcode.com/problems/longest-valid-parentheses/description/

# Pure data structures solution
import sys
from itertools import accumulate

log2 = lambda x: x.bit_length() - 1


class SparseTable:  # 0-indexed
    def __init__(self, arr, f=max, default=0):
        N = len(arr)
        self.layers = log2(len(arr)) + 1
        self.table = [[default] * self.layers for _ in range(len(arr))]
        self.f = f
        for i in range(len(arr)):  # base layer
            self.table[i][0] = arr[i]  # column 1: base cases

        for k in range(1, self.layers):  # build the rest of the table
            for i in range(N - (1 << k) + 1):
                self.table[i][k] = f(self.table[i][k - 1], self.table[i + (1 << (k - 1))][k - 1])

    def query(self, l, r):
        k = log2(r - l + 1)
        return self.f(self.table[l][k], self.table[r - (1 << k) + 1][k])


def longestValidParentheses(s: str) -> int:
    inf = 1 << 30
    arr = [1 if i == "(" else -1 for i in s]
    psa = [0] + list(accumulate(arr))
    st = SparseTable(psa, f=min, default=inf)

    # find largest [l,r]
    # with psa[l] = psa[r], min of [l,r] is at l and r, s[l] is (

    mx = max(psa)
    mi = min(psa)
    locs = [[] for _ in range(mx - mi + 1)]
    print(psa)
    for i, v in enumerate(psa):
        locs[v].append(i)

    best = 0
    for val in range(len(locs)):
        if len(locs[val]) < 2:
            continue

        prev_l = inf
        for i in range(len(locs[val]) - 1):
            l, r = locs[val][i], locs[val][i + 1]
            if st.query(l, r) == psa[l]:
                prev_l = min(prev_l, l)
                best = max(best, r - prev_l)
            else:
                prev_l = inf

    return best


print(longestValidParentheses("(())()(()(("))


# # Interval merging solution
# # - Pair up the indices of every () into [l, r]
# # - it is guaranteed that the range [l, r] is valid or else the ) would be matched with something else
# #   - eg. (() -> [1, 2] since we always match with the top of the stack
# # - remember to merge adjacent valid pairs: ()() -> [1,2],[3,4] -> [1,4]
# #
# # TC: O(nlogn)
#
# def longestValidParentheses(s: str) -> int:
#     def merge_all(intervals, sorted=False):
#         if not intervals:
#             return []
#         if not sorted:
#             intervals.sort()
#         res = [intervals[0]]
#         for l, r in intervals[1:]:
#             if res[-1][1] >= l - 1:  # left overlaps with right, we can combine, note: [1,2] + [3,4] = [1,4]
#                 res[-1] = (res[-1][0], max(res[-1][1], r))
#             else:  # disjoint intervals
#                 res.append((l, r))
#         return res
#
#     stack = []  # contains the indices of unmatched (
#     pairs = []  # matched indices of ()
#     for i, val in enumerate(s):
#         if val == "(":
#             stack.append(i)
#         elif val == ")" and stack:  # matched pair
#             pairs.append((stack.pop(), i))
#
#     best = 0
#     pairs = merge_all(pairs)
#     for l, r in pairs:
#         best = max(best, r - l + 1)
#     return best
#
#
# print(longestValidParentheses("(()())"))
