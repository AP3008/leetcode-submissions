class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        NtoL = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []

        def dfs(s,i):
            if i>=len(digits):
                res.append(s)
                return 
            for let in NtoL[digits[i]]:
                dfs(s+let,i+1)
        dfs("",0)
        return res