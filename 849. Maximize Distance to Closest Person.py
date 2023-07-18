def maxDistToClosest(seats):
    first = 0
    second = 0
    count = 0
    while count < len(seats):
        for i in range(len(seats) - 1):
            if seats[i] == 1:
                first = i

        for j in range(len(seats) - 1):
            if seats[j] == 2:
                second = j

        distance = (i - j)



seats = [1,0,0,0,1,0,1]
print(maxDistToClosest(seats))