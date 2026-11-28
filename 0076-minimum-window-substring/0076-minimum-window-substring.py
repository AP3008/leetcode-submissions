class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # We want to store our string in res, and store a res length var. So we can see if there are improvements. 
        # We use a freq. map for t, and another for s, we only add keys and values to s if that char at s[r] is in t map.  
        # The condition to shrink the window, will be when a valid string is found. In that case we increment the left pointer and add whatever that char was back to the freq. map t. 
        # Every time we have a valid combination we can compare res length to r-l+1 and if it is smaller we update res. 
        # We can find a valid combination when the hashmaps, of t and s match. To make sure this condition is met we have to delete keys in s when they reach 0 so we don't get false positives. or any funny business. 

        freqT = {}
        for c in t:
            freqT[c] = freqT.get(c, 0)+1 

        res = ""
        resLength = float('inf')
        freqS = {}
        l = 0
        for r in range(len(s)):
            if s[r] in freqT:
                freqS[s[r]] = freqS.get(s[r], 0) + 1
            while all(freqS.get(c,0) >= freqT[c] for c in freqT):
                if r-l+1 < resLength:
                    resLength = r-l+1
                    res = s[l:r+1]
                if s[l] in freqS:
                    freqS[s[l]]-=1
                l+=1 
        return res
                



