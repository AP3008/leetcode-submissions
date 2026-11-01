class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
       # Perform BFS on all rotten oranges, and then see how many BFS calls we had to make to find the minutes. Have a set of fruit to keep track and make sure the len is 0 at the end, or for better sapce and time just use a fruits counter. First create a deque() with all of the rotten fruits and perform bfs on it, also keep track of the fruits seen and turn fruits to rotten oranges when seen in bfs. 

        minutes = 0
        fruits = 0
        q = deque()

        ROW = len(grid) 
        COL = len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fruits+=1

        if not fruits: return 0  
        
        def bfs(r,c):
            nonlocal fruits
            if (r >= ROW or
                c >= COL or
                r < 0 or
                c < 0 or
                grid[r][c] == 0 or
                grid[r][c] == 2):
                return
            grid[r][c] = 2 
            fruits-=1
            q.append((r,c))


        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            minutes+=1
            if not fruits: break  

        return minutes if not fruits else -1 
