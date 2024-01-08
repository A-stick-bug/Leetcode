# https://leetcode.com/problems/count-vowels-permutation/
# 2D DP, states: current letter and position
# after each letter, there are fixed next letters, so we take the sum of dp[next letters]

def countVowelPermutation(n: int) -> int:
    after = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]
    dp = [[0] * 5 for _ in range(n)]
    dp[n - 1] = [1, 1, 1, 1, 1]  # base state: formed a valid string of length n

    for i in reversed(range(n - 1)):
        for letter in range(5):
            dp[i][letter] = sum(dp[i + 1][nxt] for nxt in after[letter]) % 1_000_000_007

    return sum(dp[0]) % 1_000_000_007


print(countVowelPermutation(5))
