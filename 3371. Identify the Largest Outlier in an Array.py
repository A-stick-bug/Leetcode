from collections import Counter


def getLargestOutlier(nums: list[int]) -> int:
    nums.sort()
    s = sum(nums)
    best = -999999999999999

    freq = Counter(nums)

    for num in nums:  # potential outlier
        freq[num] -= 1
        if (s - num) % 2 == 0:

            cur_sum = (s - num) // 2
            if freq[cur_sum] > 0:
                best = max(best, num)

        freq[num] += 1

    return best


print(getLargestOutlier(nums=[2, 3, 5, 10]))
print(getLargestOutlier([-2, -1, -3, -6, 4]))
print(getLargestOutlier([1, 1, 1, 1, 1, 5, 5]))
print(getLargestOutlier([958, 777, -746, 566, 989]))
