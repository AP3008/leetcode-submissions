class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Find the number 1 and perform bfs on it, if we find another '1' we want to switch it to '-1' so we know it has been seen. The amount of total BFS calls we make is the amount of islands that there are. We terminate bfs exploration when the index is out of bounds, a 0 has been found or a -1 is found.

        ROW, COL = len(grid), len(grid[0])
        res = 0
        def bfs(r,c):
            if (r >= ROW or 
                c >= COL or
                r < 0 or
                c < 0 or
                grid[r][c] == "0" or 
                grid[r][c] == "-1"):
                return 
            grid[r][c] = "-1"
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    bfs(r,c)
                    res+=1
        return res 