# https://leetcode.com/problems/sum-of-sortable-integers/description/
#
# - First loop all divisors of n (there are far LESS than sqrt(n) divisors)
# - We check that each 'segment' can be sorted with a cyclic shift
# - Then check that the overall result by combining each segment results in a sorted list
#
# TC: O(d(n) * n), where d(n) is the number of divisors of n
# d(n) is approx n^{1/3} in the worst case for 64-bit integers

from itertools import accumulate


class Solution:
    def sortableIntegers(self, arr: list[int]) -> int:
        n = len(arr)

        dec = [0] * n
        for i in range(n - 1):
            dec[i] = arr[i] > arr[i + 1]
        psa = [0] + list(accumulate(dec))
        query = lambda l, r: psa[r + 1] - psa[l]

        total = 0
        for k in range(1, n + 1):  # loop divisors of n
            if n % k != 0:
                continue
            if k == 1:
                total += arr == sorted(arr)
                continue

            works = True
            prev_mx = -(1 << 60)
            for i in range(0, n, k):  # check segments, this is O(n/k) * O(k) = O(n)
                l = i
                r = i + k - 1

                # check if is a cyclic shift of sorted segment
                # - cyclic shift can only have 1 decreasing index
                # - endpoints must be consistent as well
                if query(l, r - 1) == 0 or (query(l, r - 1) == 1 and arr[l] >= arr[r]):
                    ...
                else:
                    works = False
                    break

                # check consistency with previous segment
                cur_mi = min(arr[l:r + 1])
                if cur_mi < prev_mx:
                    works = False
                    break
                prev_mx = max(arr[l:r + 1])

            if works:
                total += k

        return total
