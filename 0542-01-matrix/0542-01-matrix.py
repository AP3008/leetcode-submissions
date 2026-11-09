class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # Distance, i.e shortest path, from 1 to 0, we can use a BFS algo. 
        # We add all of the zeros to a queue, and perform a dfs changing all of the 1's to the distance. We will have a result matrix with the actual distances at each index, so we can mark 1's as seen on the actual matrix so the sapce becomes O(m*n), Also the time complexity of seeing all values in a queue then performing a BFS on them will be O((m*n)^2)

        ROW, COL = len(mat), len(mat[0])
        res = [[0 for _ in range(COL)] for _ in range(ROW)]
        q = deque() 
        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    q.append((r,c,1))
                else:
                    res[r][c] = float('inf')
        
        def bfs(r,c,dist):
            if (r >= ROW or 
                c >= COL or 
                r < 0 or 
                c < 0 or
                mat[r][c] != 1):
                return 
            res[r][c] = min(res[r][c], dist)
            mat[r][c] = -1
            q.append((r,c,dist+1))
        while q:
            r,c,dist = q.popleft()
            bfs(r+1,c,dist)
            bfs(r-1,c,dist)
            bfs(r,c+1,dist)
            bfs(r,c-1,dist)
        return res 