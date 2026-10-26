class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        seen = {}
        for c in magazine:
            seen[c] = seen.get(c,0)+1 
        for c in ransomNote:
            if c in seen and seen[c] > 0:
                seen[c]-=1
            else:
                return False 
        return True 
         
