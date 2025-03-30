"""
https://leetcode.com/problems/count-beautiful-numbers/description/
Count numbers in [l,r] where product of digits is divisible by the sum
6D Digit DP, try each possible sum and product
Possible sums: 9*9 = 81
Possible products: not sure, apparently not that much

Note: we need an extra state that represents whether we are still doing
      leading zeros as those don't contribute to the product

Not sure why is this faster than trying all sums independently and doing product (mod sum)
This would technically result in only 81^2 possible `product` values
"""


def beautifulNumbers(l: int, r: int) -> int:
    n = max(len(str(l)), len(str(r)))
    sl = list(map(int, str(l).zfill(n)))
    sr = list(map(int, str(r).zfill(n)))

    cache = {}

    def solve(touch_l, touch_r, idx, added, product, zeros):
        if idx == n:  # fully constructed number state
            return product % added == 0

        state = (touch_l, touch_r, idx, added, product, zeros)  # cache
        if state in cache:
            return cache[state]

        total = 0

        low = sl[idx] if touch_l else 0
        high = sr[idx] if touch_r else 9
        for d in range(low, high + 1):
            new_zeros = zeros and d == 0  # check if still leading zeros
            total += solve(touch_l and d == sl[idx],
                           touch_r and d == sr[idx],
                           idx + 1,
                           added + d,
                           1 if new_zeros else product * d,
                           new_zeros)

        cache[state] = total
        return cache[state]

    return solve(True, True, 0, 0, 1, True)


print(beautifulNumbers(20, 100))
print(beautifulNumbers(10, 20))
print(beautifulNumbers(1, 15))


# alternate solution that TLEs, fixes the target sum beforehand and tries all possible
class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        n = max(len(str(l)), len(str(r)))
        sl = list(map(int, str(l).zfill(n)))
        sr = list(map(int, str(r).zfill(n)))

        def solve(touch_l, touch_r, idx, added, product, zeros):
            if added > target:  # went over
                return 0
            if idx == n:  # fully constructed number state
                return product == 0 and added == target

            state = (touch_l, touch_r, idx, added, product, zeros)  # cache
            if state in cache:
                return cache[state]

            total = 0

            low = sl[idx] if touch_l else 0
            high = sr[idx] if touch_r else 9
            for d in range(low, high + 1):
                new_zeros = zeros and d == 0
                total += solve(touch_l and d == sl[idx],
                               touch_r and d == sr[idx],
                               idx + 1,
                               added + d,
                               1 if new_zeros else product * d % target,
                               new_zeros)

            cache[state] = total
            return cache[state]

        total = 0
        for target in range(1, 9 * n + 1):
            cache = {}
            total += solve(True, True, 0, 0, 1, True)
        return total
