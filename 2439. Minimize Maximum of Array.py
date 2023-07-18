def minimizeArrayValue(nums):
    sum = 0
    answer = 0
    for i in range(len(nums)):
        sum += nums[i]
        answer = max(answer, (sum + i) // (i + 1))
    return answer


print(minimizeArrayValue([3,7,1,6]))