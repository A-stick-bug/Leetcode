# https://leetcode.com/problems/choose-k-elements-with-maximum-sum
# maintain sortedlist and keep track of sum of top k

from typing import List
from sortedcontainers import SortedList


def findMaxSum(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    n = len(nums1)
    arr = [(nums1[i], nums2[i], i) for i in range(n)]
    arr.sort()

    res = [0] * n
    cur = SortedList([])
    cur_s = 0

    for i in range(n):
        if i != 0 and arr[i][0] == arr[i - 1][0]:
            res[arr[i][2]] = res[arr[i - 1][2]]
        else:
            res[arr[i][2]] = cur_s

        # update cur
        val = arr[i][1]
        if len(cur) < k:
            cur_s += val
        else:
            if cur[-k] < val:
                cur_s -= cur[-k]
                cur_s += val
        cur.add(val)
    return res
