nums = [3,2,4]
target = 6

to_return = []
first_index = 0

active = True

for i in nums:
    second_index = 0

    for j in nums:
        if i + j == target and first_index != second_index:
            to_return.append(first_index)
            to_return.append(second_index)
            active = False
            break

        second_index += 1

    first_index += 1

    if not active:
        break

print(to_return)