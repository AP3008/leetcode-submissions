class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        seen = {}
        seen2 = {}
        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1
            seen2[t[i]] = seen2.get(t[i],0) + 1
        
        return seen == seen2