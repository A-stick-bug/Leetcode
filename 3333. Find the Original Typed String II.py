# https://leetcode.com/problems/find-the-original-typed-string-ii
# Combinatorics DP with PSA optimization (and constant optimization because Python is slow)
#
# - When we see a group of same chars, it must have been typed at least once
#    - anywhere from 1 to len(group) is possible
# - We have X ways of choosing if there are X chars in the group
# - Use complementary counting to minus the combinations with sum < K
#
# TC: O(NK)

from itertools import accumulate


def possibleStringCount(word: str, k: int) -> int:
    MOD = 10 ** 9 + 7

    # group consecutive together, we only care about their length
    group = [1]
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            group[-1] += 1
        else:
            group.append(1)

    n = len(group)

    # first get total number of ways
    total = 1
    for sz in group:
        total *= sz
        total %= MOD

    # all combinations have length >= k (nothing to subtract)
    if n >= k:
        return total

    target = k - n  # account for mandatory

    # dp[idx][cur_sum] = ways
    # up to not including target
    dp = [[0] * target for _ in range(n)]
    group = [i - 1 for i in group]

    for i in range(min(target, group[0] + 1)):
        dp[0][i] = 1
    for idx in range(1, n):
        psa = [0] + list(accumulate(dp[idx - 1], func=lambda x, y: x + y % MOD))
        query = lambda l, r: (psa[r + 1] - psa[l]) % MOD

        for cur_s in range(target):
            # transition, sum(dp[i-group[idx]: i+1])
            dp[idx][cur_s] = (dp[idx][cur_s] + query(max(0, cur_s - group[idx]), cur_s)) % MOD

    less_k = sum(dp[-1])
    return (total - less_k) % MOD


print(possibleStringCount(word="aaa", k=3))
print(possibleStringCount(word="aabbccdd", k=7))
print(possibleStringCount(word="aabbccdd", k=8))
print(possibleStringCount(word="aaabbb", k=3))
