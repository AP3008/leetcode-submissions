class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # This is a bfs problem, where we just mark the servers as connected on each dive. We mark seen servers as -1, so we don't double count, by checking each valid connecion. similar to islands problems. 

        # I have completley misunderstood this question, it is checking if there are any on the same row or colums 

        # If we encounter a row or column, we just use a hashset that takes in the row and it has a true or false as the value for each row, 

        #[[1,0,0,1,0],
        #[0,0,0,0,0],
        #[0,0,0,1,0]] 
        # ans: 3 connected 
        # Brute force idea to count the number or servers in each row and col, then iterate through again, if the amount of servers in that row or column is greater than 1 we can increment the res by 1 

        ROW, COL = len(grid), len(grid[0])
        row = [0] * ROW
        col = [0] * COL

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    row[r] += 1
                    col[c] += 1
        res = 0 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (row[r] > 1 or col[c] > 1):
                    res+=1 
        return res 




                        
