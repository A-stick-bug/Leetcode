def minimumTotal(triangle) -> int:  # solution using tabulation (bottom up)
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]  # left column

            elif j == i:  # right column
                triangle[i][j] += triangle[i-1][j-1]

            else:
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i-1][j])

    return min(triangle[-1])


def flip_triangle_solution(triangle) -> int:
    # smarter solution
    # flipping the triangle upside-down and applying the same logic will make the code much easier
    # you don't have to worry about the cases where it goes out of bounds

    for i in reversed(range(len(triangle)-1)):  # start from bottom
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0]


print(flip_triangle_solution(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
