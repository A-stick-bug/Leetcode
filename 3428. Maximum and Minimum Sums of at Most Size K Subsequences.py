# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences
# combinatorics question
# Precompute the first 100 columns of Pascal's triangle with 10^5 rows

MOD = 10 ** 9 + 7
MN = 10 ** 5 + 1

res = []
for i in range(MN):
    row = [1] * min(102, i + 1)
    for j in range(1, min(101, i)):
        row[j] = (res[i - 1][j - 1] + res[i - 1][j]) % MOD
    res.append(row)


def minMaxSums(nums: list[int], k: int) -> int:
    n = len(nums)

    nums.sort()
    total = 0
    for i, num in enumerate(nums):
        rem = n - i - 1
        total += num * 2
        for pick in range(1, min(k, rem + 1)):
            total += num * res[rem][pick] % MOD
            total %= MOD

        rem2 = i

        for pick in range(1, min(k, rem2 + 1)):
            total += num * res[rem2][pick] % MOD
            total %= MOD
    return total % MOD


print(minMaxSums(nums=[1, 2, 3], k=2))
print(minMaxSums(nums=[5, 0, 6], k=1))
print(minMaxSums(nums=[1, 1, 1], k=2))
