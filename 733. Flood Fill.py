def floodFill(image, sr: int, sc: int, color: int):
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]):
            return
        if image[row][col] != start or image[row][col] == color:
            return
        image[row][col] = color
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    start = image[sr][sc]
    dfs(sr,sc)
    return image


img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(floodFill(img, 1, 1, 7))
