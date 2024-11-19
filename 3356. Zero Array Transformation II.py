# https://leetcode.com/problems/zero-array-transformation-ii/description/
# binary search with different array to check if the first `mid` queries work

from itertools import accumulate


def minZeroArray(nums: list[int], queries: list[list[int]]) -> int:
    n = len(nums)
    q = len(queries)

    def works(queries: list[list[int]]) -> bool:  # copied from LC. 3355
        diff = [0] * (n + 1)
        for l, r, val in queries:
            diff[l] += val
            diff[r + 1] -= val
        dec = list(accumulate(diff))
        return all(dec[i] >= nums[i] for i in range(n))

    low = 0
    high = q
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if works(queries[:mid]):  # check if the first `mid` queries work
            high = mid - 1
            ans = mid  # it works, update answer
        else:
            low = mid + 1
    return ans


print(minZeroArray(nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
print(minZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]))
print(minZeroArray([7, 6, 8], [[0, 0, 2], [0, 1, 5], [2, 2, 5], [0, 2, 4]]))
