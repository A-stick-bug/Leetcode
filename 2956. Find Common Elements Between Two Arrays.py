from typing import List


def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
    first = sum(i in nums2 for i in nums1)
    sec = sum(i in nums1 for i in nums2)
    return [first, sec]


print(findIntersectionValues(nums1=[3, 4, 2, 3], nums2=[1, 5]))
