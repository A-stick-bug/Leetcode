# simple greedy approach, O(n)
# basically just find the number of times that the sequences goes from increase to decreasing and vice versa
# the actual difference between numbers is ignored

def wiggleMaxLength(nums) -> int:
    res = 1
    prev = 0  # 0 is default, 1 means decreasing, 2 means increasing

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:  # if 2 consecutive numbers are the same, we just ignore it
            continue
        elif nums[i] > nums[i-1] and (prev == 1 or prev == 0):  # the last sequence was decreasing, now increasing
            prev = 2
            res += 1
        elif nums[i] < nums[i-1] and (prev == 2 or prev == 0):  # the last sequence was increasing, now decreasing
            prev = 1
            res += 1
    return res


print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
