class Solution:
    def checkString(self, s: str) -> bool:
        # binary search for a b that appears in before a. 
        # 1. If s[m] == 'a' we can 
        flag = False
        for i in range(len(s)):
            if s[i] == 'b': flag = True
            if flag and s[i] == 'a': return False
        return True
            