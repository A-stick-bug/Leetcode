def countSubIslands(self, grid1, grid2):
    ROWS = len(grid1)
    COLS = len(grid1[0])

    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    visited = [[False for _ in range(COLS)] for i in range(ROWS)]

    def dfs(row,col):
        if 0 > row >= ROWS or 0 > col >= COLS or visited[row][col] or grid2[row][col] == 0:
            return
        if grid1[row][col]
        for r,c in directions:
            dfs(row+r,col+c)