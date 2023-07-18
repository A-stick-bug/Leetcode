def twoSum(numbers, target):
    start, end = 0, len(numbers) - 1

    while True:
        if numbers[start] + numbers[end] > target:
            end -= 1
        elif numbers[start] + numbers[end] < target:
            start += 1
        else:
            return [start + 1, end + 1]
