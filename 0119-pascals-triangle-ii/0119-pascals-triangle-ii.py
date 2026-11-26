class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # We only keep track of the row above and the current row. We return the last row we get to. 

        above = [0,1,0] # The final answer will be above[1:len(above)-1]
        rows = 1
        while rowIndex >= 0:
            curr = [0]*(rows+2)
            for i in range(1, len(curr)-1):
                curr[i] = above[i-1] + above[i]
            rows+=1 
            above = curr
            rowIndex -= 1
        return above[1:len(above)-1]
