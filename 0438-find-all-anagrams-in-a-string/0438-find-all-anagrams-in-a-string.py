class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # We can use a sliding window where we look at a string and increment the right pointer to see if we can get an anagram from this index. We do this for every index. We can compare by checking that our window essentially has the same hashmap as p, if it doesn't we break out of the window and continue to the next index, if we find one, we want to 
        if len(s) < len(p): return []
        Pctr = {}
        res = [] 
        for c in p:
            Pctr[c] = Pctr.get(c,0)+1 
        
        l = 0 
        curr = {}
        for r in range(len(s)):
            curr[s[r]] = curr.get(s[r], 0)+1 
            if r - l + 1 > len(p):
                curr[s[l]] -= 1
                # We need to delete the keys that aren't being used anymore, if we want to properly compare the Pctr, otherwise the check for a the matching hashmap will always return false because of dangling keys. 
                if curr[s[l]] == 0:
                    del curr[s[l]]
                # We increment the window, on
                l+=1 
            if r - l + 1 == len(p):
                if curr == Pctr:
                    res.append(l)
        return res 
        