def hasTrailingZeros(nums: list[int]) -> bool:
    cnt = 0
    for i in nums:
        cnt += i % 2 == 0

    return cnt >= 2


print(hasTrailingZeros(nums = [1,2,3,4,5]))
