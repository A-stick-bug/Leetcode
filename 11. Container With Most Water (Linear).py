# linear time with 2 pointers, write better loop conditions and use min/max()

def most_water(height):
    index1 = 0
    index2 = len(height) - 1
    most = 0

    while index1 < index2:
        area = min(height[index1], height[index2]) * (index2 - index1)
        most = max(most,area)

        #  if the value of first index is less than the value of last index increase the first index else decrease the last index
        if height[index1] < height[index2]:
            index1 += 1

        else:
            index2 -= 1

    return most


height = [2, 3, 4, 5, 18, 17, 6]
print(most_water(height))
