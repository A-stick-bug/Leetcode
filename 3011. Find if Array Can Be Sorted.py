# simulate bubble sort

def canSortArray(nums: list[int]) -> bool:
    def cnt(num):
        b = bin(num)[2:]
        return b.count("1")

    s = sorted(nums)
    n = len(nums)
    for _ in range(n):
        for i in range(1, n):
            if nums[i] < nums[i - 1] and cnt(nums[i]) == cnt(nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums == s
