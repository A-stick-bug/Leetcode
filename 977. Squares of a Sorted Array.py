# two pointer: start one pointer at start, one at end

def sortedSquares(nums):
    nums = list(map(abs,nums))
    arr = []

    first = 0
    second = len(nums) - 1

    for i in range(len(nums)):
        if nums[first] > nums[second]:
            arr.insert(0, nums[first]**2)
            first += 1
        else:
            arr.insert(0, nums[second]**2)
            second -= 1

    return arr


nums = [-5,-3,-2,-1]
print(sortedSquares(nums))
