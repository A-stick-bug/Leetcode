from math import gcd
from functools import reduce

def minOperations(nums):
    n = len(nums)
    if 1 in nums:
        return n - 1
    g = reduce(gcd, nums)
    if g > 1:
        return -1
    res = 0
    for i in range(n - 1):
        while nums[i] != 1:
            nums[i + 1] = gcd(nums[i], nums[i + 1])
            res += 1
            if nums[i + 1] == 1:
                break
    return res
nums =[2,6,3,4]
print(minOperations(nums))