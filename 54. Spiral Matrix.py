
def spiralOrder(matrix):
    out = []
    while True:
        try:
            out += matrix.pop(0)

            for rows in matrix:
                out.append(rows.pop())

            out += matrix.pop()[::-1]

            for rows in matrix[::-1]:
                out.append(rows.pop(0))
        except:
            return out


print(spiralOrder([[7],[9],[6]]))