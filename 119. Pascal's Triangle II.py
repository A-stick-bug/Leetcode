# iterative solution
def getRow(rowIndex: int):
    if rowIndex == 0:
        return [1]

    prev = [1, 1]
    for i in range(1, rowIndex):
        row = [1]  # left side is all 1
        for j in range(1, len(prev)):  # fill in middle rows
            row.append(prev[j] + prev[j - 1])

        row.append(1)  # right side is all 1
        prev = row.copy()  # update row

    return prev


print(getRow(0))
