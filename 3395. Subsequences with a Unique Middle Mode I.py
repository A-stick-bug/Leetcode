# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i
# annoying counting problem with lots of casework
# We need 5 numbers in the subsequence, consider all possible middle numbers
# and use casework + combinatorics to check what can be on the left and right

from collections import Counter


def subsequencesWithMiddleMode(nums: list[int]) -> int:
    n = len(nums)
    MOD = 10 ** 9 + 7

    # freq for left and right side of current mid
    freq_r = Counter(nums[1:])
    freq_l = Counter()
    total = 0

    for i in range(n):
        len_l = i
        len_r = n - i - 1

        if i >= 2 and i < n - 2:
            # for these, _ represents anything that is not `a`
            # order DOES NOT matter

            # case 1: [[a, _], a, [a, _]]
            cur = nums[i]
            total += freq_l[cur] * freq_r[cur] * (len_l - freq_l[cur]) * (len_r - freq_r[cur])

            # case 1.1: [[a,a],a,[a,_]]
            total += (freq_l[cur] - 1) * freq_l[cur] // 2 * freq_r[cur] * (len_r - freq_r[cur])

            # case 1.2: [[a,_],a,[a,a]]
            total += (freq_r[cur] - 1) * freq_r[cur] // 2 * freq_l[cur] * (len_l - freq_l[cur])

            # case 1.3: [[a,a],a,[a,a]]
            total += (freq_l[cur] * (freq_l[cur] - 1)) // 2 * (freq_r[cur] * (freq_r[cur] - 1)) // 2

            # case 1.4: [[a,a],a,[_,_]]
            r = len_r - freq_r[cur]
            total += (freq_l[cur] * (freq_l[cur] - 1)) // 2 * (r * (r - 1)) // 2

            # case 1.5: [[_,_],a,[a,a]]
            l = len_l - freq_l[cur]
            total += (freq_r[cur] * (freq_r[cur] - 1)) // 2 * (l * (l - 1)) // 2

            # case 2: [[b, a], a, [c, d]]
            # try all values of `b`
            # removed cases since `c` cannot equal `d`
            dups = sum(v * (v - 1) // 2 for k, v in freq_r.items() if k != cur)
            for b, v in freq_l.items():
                if b == cur:
                    continue
                le_r = len_r - freq_r[cur] - freq_r[b]  # can't use `a` and `b` on other side
                # note: we are adding back the pairs formed with `b` since they are ignored in the first place
                total += freq_l[cur] * v * (le_r * (le_r - 1) // 2 - dups + freq_r[b] * (freq_r[b] - 1) // 2)

            # case 3: [[c, d], a, [b, a]]
            dups = sum(v * (v - 1) // 2 for k, v in freq_l.items() if k != cur)
            for b, v in freq_r.items():
                if b == cur:
                    continue
                le_l = len_l - freq_l[cur] - freq_l[b]
                total += freq_r[cur] * v * (le_l * (le_l - 1) // 2 - dups + freq_l[b] * (freq_l[b] - 1) // 2)

        total %= MOD

        freq_l[nums[i]] += 1  # update left and right
        if i != n - 1:
            freq_r[nums[i + 1]] -= 1

    return total


print(subsequencesWithMiddleMode([0, -1, 0, -1, -1]))  # 0
print(subsequencesWithMiddleMode([0, 1, -1, -1, -1]))  # 1
print(subsequencesWithMiddleMode([0, 1, 0, 1, -1]))  # 0

print(subsequencesWithMiddleMode(nums=[1, 1, 1, 1, 1, 1]))  # 6
print(subsequencesWithMiddleMode(nums=[1, 2, 2, 3, 3, 4]))  # 4
print(subsequencesWithMiddleMode(nums=[0, 1, 2, 3, 4, 5, 6, 7, 8]))  # 0
