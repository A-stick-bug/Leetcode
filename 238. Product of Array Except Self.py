# the trivial way would be to just find the product of all elements and divide but the problem says not to do so
# therefore, we use a prefix sum (well a prefix product in this case) for both the left and right
# note: handle the first and last elements seperately to prevent index out of bounds

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    product_left = [0 for _ in range(n)]
    product_left[0] = nums[0]  # prevent error for i = 0 by starting at 1
    for i in range(1, n):
        product_left[i] = product_left[i - 1] * nums[i]

    product_right = [0 for _ in range(n)]
    product_right[-1] = nums[-1]  # prevent out of bounds for last value
    for i in reversed(range(n - 1)):
        product_right[i] = product_right[i + 1] * nums[i]

    res = []
    for i in range(n):
        left = 1 if i == 0 else product_left[i - 1]
        right = 1 if i == n - 1 else product_right[i + 1]
        res.append(left * right)

    return res


print(productExceptSelf([1, 2, 3, 4]))
