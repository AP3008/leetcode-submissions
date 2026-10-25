class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        res = [""] * len(s)

        l, r = 0, len(s)-1
        while l <= r:
            while s[l] not in vowels:
                res[l] = s[l]
                l+=1
                if l >= len(s)-1:
                    return s
            while s[r] not in vowels:
                res[r] = s[r]
                r-=1 
                if r <= 0:
                    return s
            res[l], res[r] = s[r], s[l]
            l+=1 
            r-=1
        return "".join(res)