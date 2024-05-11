# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/
# partition DP
# let dp[i] be the minimum number of partitions including everything up to i

from collections import Counter


def minimumSubstringsInPartition(s: str) -> int:
    s = "!" + s
    n = len(s)
    inf = 10000
    dp = [inf] * n
    dp[0] = 0

    for i in range(1, n):
        freq = Counter()
        freq[s[i]] += 1
        for j in reversed(range(i)):  # look for valid transitions from previous values
            if len(set(freq.values())) == 1:
                dp[i] = min(dp[i], dp[j] + 1)
            freq[s[j]] += 1
    return dp[-1]


print(minimumSubstringsInPartition(s="fabccddg"))
print(minimumSubstringsInPartition(s="abababaccddb"))
