# https://leetcode.com/problems/next-special-palindrome-number/
# Optimized brute force, prune as much of the search space as possible
# Note: this solution is a bit overkill, you don't need all these optimizations
#
# Optimizations:
# 1. Precompute the partitions for each number length
# 2. Answer has equal or 1 more digit than the input, only try these partitions
# 3. Only care about the smallest permutation that is >n for each partition, similar to digit DP
#
# We don't bother with time complexities as constant factors absolutely dominate

nums = list(range(1, 10))
parts = [[] for _ in range(18)]
for mask in range(1 << 9):
    res = []
    for bit in range(9):
        if mask & (1 << bit):
            res.append(bit + 1)
    odds = sum(i % 2 == 1 for i in res)
    if odds > 1:  # can't have more than 1 odd since it must go in the center
        continue
    if sum(res) < len(parts):
        parts[sum(res)].append(res)


# for i in range(17):
#     print(i, parts[i], len(parts[i]))


def specialPalindrome(n: int) -> int:
    n += 1  # >=
    n_str = list(map(int, str(n)))
    le = len(n_str)

    best = float("inf")

    def get_best_partition(le, num):
        """Returns the minimum answer of length `le` that is >`num`"""
        nonlocal best
        for partition in parts[le]:
            freq = [0] * 10
            for i in partition:
                freq[i] = i // 2

            vis = [set(), set()]
            vis[0].add(tuple(freq))
            stack = [(freq, [], False)]
            while stack:
                state, cur, ge = stack.pop()

                if len(cur) == le // 2:
                    if le % 2 == 0:
                        actual = cur + cur[::-1]
                    else:
                        odd = [i for i in partition if i % 2 == 1][0]
                        actual = cur + [odd] + cur[::-1]
                    ans1 = int("".join(map(str, actual)))
                    if ans1 >= n:
                        best = min(best, ans1)
                    continue

                idx = len(cur)
                for i in reversed(range(1, 10)):
                    if state[i] > 0 and (i >= num[idx] or ge):
                        new_ge = ge or i > num[idx]
                        new_state = state.copy()
                        new_state[i] -= 1  # use twice due to mirroring
                        new_cur = cur.copy()
                        new_cur.append(i)
                        if tuple(new_state) in vis[new_ge]:
                            continue
                        vis[new_ge].add(tuple(new_state))
                        stack.append((new_state, new_cur, new_ge))

    get_best_partition(le, n_str)
    get_best_partition(le + 1, [0] + n_str)
    return best


print(specialPalindrome(4774))  # 23332
print(specialPalindrome(2))  # 22
print(specialPalindrome(33))  # 212
print(specialPalindrome(502))  # 4444
