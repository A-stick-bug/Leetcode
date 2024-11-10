# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n
# Digit DP and observations
# For each `i` in [1, 800] if it can be reduced to 1 in less than k moves
# all numbers `x` with `i` set bits are valid since you can go `x` -> `i` -> ... -> 1 in <=k moves
# dp[touch_r][idx][set bits]: count of valid numbers with current one as a prefix

MN = 801
reductions = [-1] * MN
reductions[1] = 0
for i in range(2, MN):
    reductions[i] = reductions[i.bit_count()] + 1


def countKReducibleNumbers(s: str, k: int) -> int:
    le = len(s)
    MOD = 10 ** 9 + 7
    s = list(map(int, s))

    cache = [[[-1] * (le + 1) for _ in range(le)] for _ in range(2)]
    valid = {i for i in range(1, MN) if reductions[i] < k}

    def solve(touch_r, idx, bits):
        """
        Count how many numbers <n have a valid number of set bits
        A number is valid if the number of moves to reduce it to 1 is <k
        """
        nonlocal cache
        if idx == le:  # finish making number, check if valid
            return bits in valid and not touch_r
        if cache[touch_r][idx][bits] != -1:  # cache
            return cache[touch_r][idx][bits]

        t = 0
        upper = s[idx] if touch_r else 1
        for dig in range(upper + 1):  # standard digit dp transitions
            t += solve(touch_r and s[idx] == dig, idx + 1, bits + dig)
        cache[touch_r][idx][bits] = t % MOD
        return cache[touch_r][idx][bits]

    return solve(True, 0, 0) % MOD


print(countKReducibleNumbers(s="111", k=1))
print(countKReducibleNumbers(s="1000", k=2))
print(countKReducibleNumbers(s="1", k=3))
