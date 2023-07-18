from typing import List

def wiggleSort(nums: List[int]) -> None:
    # bubble sort solution where elements are switched based on index
    for i in range(len(nums) - 1):
        if i % 2 == 0:  # even index
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]  # swap values

        else:  # odd index
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    #return nums


nums = [3,5,2,1,6,4]
print(wiggleSort(nums))