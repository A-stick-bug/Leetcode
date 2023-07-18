def threeSum(nums):
    def find_pairs(i):
        start, end = i+1, len(nums) - 1

        while True:
            sum = nums[i] + nums[start] + nums[end]
            if sum > 0:
                end -= 1
            elif sum < 0:
                start += 1
            else:
                res.append([])

    nums.sort()
    res = []
    for i in range(len(nums)):
