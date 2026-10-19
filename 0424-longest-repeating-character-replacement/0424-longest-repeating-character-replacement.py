class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # Sliding window 
        n = len(s)
        freq = [0] * 26
        l = r = 0
        maxLen = maxFreq = 0 

        while r < n:
            c = s[r]
            freq[ord(c)-ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(c)-ord('A')])

            if (r-l+1) - maxFreq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l+=1 
            
            maxLen = max(maxLen, r-l+1)
            r+=1 
        return maxLen 