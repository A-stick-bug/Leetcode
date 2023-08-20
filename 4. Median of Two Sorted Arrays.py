# to do
from  typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    x = nums1 + nums2
    x.sort()
    mid = len(x) // 2

    if len(x) % 2 == 1:
        return x[mid]
    else:
        return (x[mid] + x[mid - 1]) / 2
