class Solution:
    def myAtoi(self, s: str) -> int:    
        i = 0
        n = len(s)
        sign = 1
        res = 0
        LOWER_BOUND = -(2**31)
        UPPER_BOUND = 2**31-1
        # Skip leading whitespaces
        while i < n and s[i] == " ":
            i+=1
        
        # determine sign
        if i < n and s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i+=1 
        limit = 2**31 if sign == -1 else UPPER_BOUND
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            i+=1 
        return min(UPPER_BOUND, max((res * sign), LOWER_BOUND))
