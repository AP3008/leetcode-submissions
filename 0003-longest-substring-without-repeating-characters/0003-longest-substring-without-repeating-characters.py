class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) <= 1:
            return len(set(s)) 

        l = 0 
        maxLength = 1 
        #for i in range(1, len(s)):
        #    while s[i] in s[l:i]:
        #        l+=1 
        #    distance = i - l+1 
        #    maxLength = max#(maxLength, distance)
        #return maxLength 

        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1 
            seen.add(s[i])
            maxLength = max(maxLength, i-l+1)
        return maxLength
            



