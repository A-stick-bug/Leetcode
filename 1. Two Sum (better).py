from collections import defaultdict


def twoSum(nums, target):
    map = defaultdict(int)

    for index, num in enumerate(nums):
        other = target - num
        if other in map:
            return [map[other], index]

        map[num] = index

    return [-1, -1]

nums =[2,7,11,15]
target = 17

print(twoSum(nums, target))