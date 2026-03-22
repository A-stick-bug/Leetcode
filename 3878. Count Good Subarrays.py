# https://leetcode.com/problems/count-good-subarrays/description/
# Precomputation + optional data structures
#
# At each index i, we count the number of subarrays with arr[i] as the OR value
# - Check how far we can extend left and right
# - Here, we use a sparse table to query OR values
#   - we can also use a monotonic stack over all individual bits
# - To avoid overcounting, ensure the left bound never exceeds a previous equal element


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


def countGoodSubarrays(nums: list[int]) -> int:
    n = len(nums)

    prev_eq = [-1] * n  # prev_eq[i] = closest previous index with value each to nums[i]
    prev_idx = {}
    for i, v in enumerate(nums):
        if v in prev_idx:
            prev_eq[i] = prev_idx[v]
        prev_idx[v] = i

    st = SparseTable(nums, f=lambda x, y: x | y, default=0)

    t = 0
    for i in range(n):
        r = n
        l = -1

        # find right bound
        low = i
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if st.query(i, mid) == nums[i]:
                r = mid
                low = mid + 1
            else:
                high = mid - 1

        # find left bound
        low = 0
        high = i
        while low <= high:
            mid = (low + high) // 2
            if st.query(mid, i) == nums[i]:
                l = mid
                high = mid - 1
            else:
                low = mid + 1

        l = max(l, prev_eq[i] + 1)  # ensure we don't go over previous equal element
        t += (r - i + 1) * (i - l + 1)
    return t


print(countGoodSubarrays(nums=[4, 2, 3]))
