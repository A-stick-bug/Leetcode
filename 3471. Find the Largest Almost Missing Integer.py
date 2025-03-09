def largestInteger(nums: list[int], k: int) -> int:
    res = -1
    for num in sorted(nums):
        cnt = 0
        for i in range(len(nums) - k + 1):
            sub = nums[i:i + k]
            cnt += num in sub
        if cnt == 1:
            res = num
    return res
