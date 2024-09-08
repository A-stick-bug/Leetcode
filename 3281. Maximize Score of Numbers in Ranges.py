# https://leetcode.com/problems/maximize-score-of-numbers-in-ranges
# binary search answer, use greedy to check

def maxPossibleScore(start: list[int], d: int) -> int:
    n = len(start)
    start.sort()
    inf = 1 << 60

    def works(val):  # check if min diff of val works
        prev = -inf
        for i in range(n):
            if start[i] + d < prev + val:
                return False
            prev = max(start[i], prev + val)
        return True

    low = 0
    high = 10 ** 10 + 1
    while low <= high:
        mid = (low + high) // 2
        if works(mid):
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


print(maxPossibleScore(start=[6, 0, 3], d=2))
print(maxPossibleScore(start=[2, 6, 13, 13], d=5))
