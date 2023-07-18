# first attempt (brute force) O(n^3)

s = ""

letters = []
count = 1
highest = 1
empty = False

if s == "":  # empty test case
    print(0)
    empty = True

for i in s:
    first = True
    letters.append(i)

    for j in s:
        if first:
            first = False

        elif j not in letters:
            letters.append(j)
            count += 1
        elif j in letters:
            if count > highest:
                highest = count
            count = 1

            s = s[1:]
            letters = []
            break

if not empty:
    print(highest)

