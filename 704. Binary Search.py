def search(nums, target):
    low=0
    high = len(nums)-1

    while high >= low:
        mid = (high+low)//2
        if target > nums[mid]:
            low = mid + 1
        elif target == nums[mid]:
            return mid
        else:
            high = mid-1

    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))
