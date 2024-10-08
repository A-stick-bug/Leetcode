# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers
# simple greedy

def maximumTotalSum(maximumHeight: list[int]) -> int:
    maximumHeight.sort(reverse=True)
    total = 0
    prev = 1 << 60
    for i in maximumHeight:
        prev = min(i, prev - 1)
        if prev <= 0:
            return -1
        total += prev

    return total


print(maximumTotalSum(maximumHeight=[2, 3, 4, 3]))
