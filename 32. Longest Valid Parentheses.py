# https://leetcode.com/problems/longest-valid-parentheses/description/
# Interval merging
# - Pair up the indices of every () into [l, r]
# - it is guaranteed that the range [l, r] is valid or else the ) would be matched with something else
#   - eg. (() -> [1, 2] since we always match with the top of the stack
# - remember to merge adjacent valid pairs: ()() -> [1,2],[3,4] -> [1,4]
#
# TC: O(nlogn)

def longestValidParentheses(s: str) -> int:
    def merge_all(intervals, sorted=False):
        if not intervals:
            return []
        if not sorted:
            intervals.sort()
        res = [intervals[0]]
        for l, r in intervals[1:]:
            if res[-1][1] >= l - 1:  # left overlaps with right, we can combine, note: [1,2] + [3,4] = [1,4]
                res[-1] = (res[-1][0], max(res[-1][1], r))
            else:  # disjoint intervals
                res.append((l, r))
        return res

    stack = []  # contains the indices of unmatched (
    pairs = []  # matched indices of ()
    for i, val in enumerate(s):
        if val == "(":
            stack.append(i)
        elif val == ")" and stack:  # matched pair
            pairs.append((stack.pop(), i))

    best = 0
    pairs = merge_all(pairs)
    for l, r in pairs:
        best = max(best, r - l + 1)
    return best


print(longestValidParentheses("(()())"))
