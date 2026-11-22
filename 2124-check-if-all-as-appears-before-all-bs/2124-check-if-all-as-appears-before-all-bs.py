class Solution:
    def checkString(self, s: str) -> bool:
        # Just check if we find a b once we do, we need to look for an a, if we find it then we are good. 

        # Another option is run a binary search, if we find a b we need to switch l = m + 1 because we need to find an a with there, if it exists 
        # If we find an a we can check from s[l:m] if the length of the set of letters is greater than 1 if it is return false, otherweise we continue the search by tightening the window
        l, r = 0, len(s)-1
        while l < r:
            m = (l+r)//2
            if s[m] == 'b':
                if len(set(s[m:r+1])) != 1:
                    return False
                else: 
                    r = m - 1
            else:
                if len(set(s[l:m+1])) != 1:
                    return False
                else:
                    l = m +1 
        return True 
                