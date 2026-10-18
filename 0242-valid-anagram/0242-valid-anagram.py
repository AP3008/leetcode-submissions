class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        seen = {}
        seen2 = {}
        for c in s:
            seen[c] = seen.get(c, 0) + 1
        
        for c in t:
            if not seen.get(c):
                return False 
            seen2[c] = seen2.get(c, 0)+1

        return seen == seen2