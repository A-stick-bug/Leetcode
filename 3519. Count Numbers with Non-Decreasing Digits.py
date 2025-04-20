# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits
# Digit DP in other bases
# To create numbers with increasing digits, keep track of the previous digit used
# Note: no need to deal with leading zeros n > 0

from functools import cache

MOD = 10 ** 9 + 7
MP = 400
power = [[0] * MP for _ in range(11)]
for b in range(2, 11):
    power[b][0] = 1
for b in range(2, 11):
    for i in range(1, MP):
        power[b][i] = power[b][i - 1] * b


def convert_base(num, b):  # from base 10
    res = []
    started = False
    for p in reversed(range(MP)):
        cnt = 0
        while num >= power[b][p]:
            cnt += 1
            num -= power[b][p]
        if cnt != 0:
            started = True
        if started:
            res.append(cnt)
    return "".join(map(str, res))


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        l = str(convert_base(int(l), b))
        r = str(convert_base(int(r), b))
        n = max(len(l), len(r))
        l_str = list(map(int, l.zfill(n)))
        r_str = list(map(int, r.zfill(n)))

        @cache
        def solve(touch_l, touch_r, idx, prev):
            if idx == n:
                return 1

            low = max(prev, l_str[idx] if touch_l else 0)  # non-decreasing digits
            high = r_str[idx] if touch_r else b - 1
            total = 0
            for d in range(low, high + 1):
                total += solve(touch_l and d == l_str[idx],
                               touch_r and d == r_str[idx],
                               idx + 1,
                               d)
            return total % MOD

        return solve(True, True, 0, 0)
