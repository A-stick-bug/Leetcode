def isMajorityElement(nums, target):
    # find index of target
    low, high = 0, len(nums)

    while high > low:
        mid = (high+low)//2
        if target > nums[mid]:
            low = mid+1
        else:
            high = mid

    index = low

    # element cover half the length of the array to be majority
    end_index = index + len(nums)//2
    return (len(nums) > end_index) and (nums[end_index] == target)


print(isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5))
