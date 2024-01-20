# no idea why this worked, guessed it during the contest

from math import ceil
from collections import Counter


def minimumArrayLength(nums: list[int]) -> int:
    cnt = Counter(nums)
    m = cnt[min(nums)]
    option1 = (ceil(m / 2))
    small = min(nums)
    if any(num % small for num in nums):
        return 1
    else:
        return option1
