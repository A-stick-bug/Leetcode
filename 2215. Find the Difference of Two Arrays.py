from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [list(nums1 - nums2), list(nums2 - nums1)]


nums1 = [1,2,3,3]; nums2 = [1,1,2,2]
print(findDifference(nums1,nums2))
