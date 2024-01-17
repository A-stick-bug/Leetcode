# pretty much just greedy

from collections import Counter


def maximumSetSize(nums1: list[int], nums2: list[int]) -> int:
    c1 = Counter(nums1)
    c2 = Counter(nums2)

    rem1 = len(nums1) // 2  # remove duplicates first
    for k, val in c1.items():
        rem1 -= val - 1
        c1[k] = 1
    rem2 = len(nums2) // 2
    for k, val in c2.items():
        rem2 -= val - 1
        c2[k] = 1

    for key in c1:
        if rem2 <= 0:
            break
        if key in c2:
            del c2[key]
            rem2 -= 1

    for key in c2:
        if rem1 <= 0:
            break
        if key in c1:
            del c1[key]
            rem1 -= 1

    return len(set(list(c1.keys())+list(c2.keys()))) - max(0, rem1) - max(0, rem2)


print(maximumSetSize(nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]))
