# https://leetcode.com/problems/longest-balanced-substring-after-one-swap/
# Standard trick: convert 0 to -1 and aim for sum of 0
# This is a standard problem that can be solved with prefix sums and a dict
#
# Moving 1 element is trickier, essentially, you can change the 'balance' by 2 or -2
# by moving a 1 or 0 (-1) inside the range
# We will store the earliest indices that have an available 0 and 1 that you can move into your range
#
# We will solve in reverse too to consider the case of bringing a 0 or 1 from the right
#
# TC: O(n)

def longestBalanced(s: str) -> int:
    def solve(s):
        n = len(s)
        arr = [-1 if i == "0" else 1 for i in s]

        # earliest indices, direct and with swap
        first1 = {}
        first_o = {}
        first_z = {}
        first1[0] = -1
        cur = 0
        best = 0
        zero = False
        one = False
        for i in range(n):
            val = arr[i]
            if val == 1:
                one = True
            if val == -1:
                zero = True
            cur += val

            # direct
            if cur in first1:
                best = max(best, i - first1[cur])
            else:
                first1[cur] = i

            # bring in a zero
            if cur - 2 in first_z:
                best = max(best, i - first_z[cur - 2])
            if zero and cur not in first_z:
                first_z[cur] = i

            # bring in a 1
            if cur + 2 in first_o:
                best = max(best, i - first_o[cur + 2])
            if one and cur not in first_o:
                first_o[cur] = i

        return best

    return max(solve(s), solve(s[::-1]))