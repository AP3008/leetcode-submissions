class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
       # DP solution, 1D because we only need to store 2 rows at a time, the current row we are building, is based of the previous one. 

       # The entire top row will only have 1 way to reach that square, so we can use that as a base case. We want to also create a layer above of 0's to pad the outside so we don't go out of bounds. Starting from 0,0 we want to move to m,n checking the values, above it and to the left of it. Since we can only go row by row, we will only have 2 rows in memory. 

        # We add 1 to so we can check whats on the left even at index "0", our actual start index will be 1 -> n
        aboveRow = [0] * (n+1)
        currRow = [0] * (n +1)
        currRow[1] = 1
        for i in range(m):
            for j in range(1,n+1):
                currRow[j] += currRow[j-1] + aboveRow[j]
            aboveRow = currRow.copy()
            currRow = [0] * (n+1)
        return aboveRow[n]