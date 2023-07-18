# brute force (TLE), track indexes using variable and increasing by one every loop

def most_water(height):
    index1 = 0
    most = 0

    for i in height:
        first = True
        index2 = 0

        for j in height:
            if first:
                first = False

            else:
                l = index2 - index1
                h = min(i, j)

                area = l * h

                if area > most:
                    most = area

            index2 += 1

        index1 += 1

    return most


height = [1, 0, 0, 0, 0, 0, 0, 2, 2]
print(most_water(height))
