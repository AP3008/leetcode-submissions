class Solution:
    def longestPalindrome(self, s: str) -> str:
        # another sliding window 
        if not s:
            return ""

        def expandCenter(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return r-l-1
        
        start = end = 0

        for i in range(len(s)):
            odd = expandCenter(s,i,i)
            even = expandCenter(s,i,i+1)
            maxLen = max(odd, even)
            if maxLen > end - start:
                start = i - (maxLen-1) // 2
                end = i + maxLen // 2
        return s[start:end+1]