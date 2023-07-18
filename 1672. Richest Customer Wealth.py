accounts = [[1, 2, 3, 4], [1, 2, 3, 4, 5]]
values = []

highest = 0

for i in accounts:
    current = sum(i)
    if current > highest:
        highest = current


print(highest)
