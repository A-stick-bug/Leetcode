# you don't need to simulate, just make observations
# a PSA or sliding window can be used to optimize to O(n)

def countValidSelections(nums: list[int]) -> int:
    t = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            continue
        l = sum(nums[:i])
        r = sum(nums[i:])

        if l == r:
            t += 2
        elif l + 1 == r or l == r + 1:
            t += 1
    return t


print(countValidSelections(nums=[4, 0, 0, 0, 3]))
print(countValidSelections(nums=[2, 3, 4, 0, 4, 1, 0]))
