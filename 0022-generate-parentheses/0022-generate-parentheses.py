class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # This can be solved easily with backtracking, Breaking the decision tree down, you can either append an open bracket, or an open and closed bracket. Since n is small < 10, backtracking seems like the logical approach. We take a backtrack function that takes in a count of open brackets and closed. We append an iteration once both numbers equal n.

        curr = []
        res = [] 
        def backtrack(open, closed):
            if open == n and closed == open:
                res.append("".join(curr))
                return 
            if open < n:
                curr.append("(")
                backtrack(open+1, closed)
                curr.pop()
            if closed < open:
                curr.append(")") 
                backtrack(open, closed+1)
                curr.pop()
        backtrack(0,0)
        return res
            