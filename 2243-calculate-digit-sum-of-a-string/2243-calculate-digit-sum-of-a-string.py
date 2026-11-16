class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            q = deque()
            counter = 0 
            total = 0 
            res = ""
            for i in range(len(s)):
                total += int(s[i])
                counter+=1 
                if (counter >= k) or (i == len(s)-1):
                    res += str(total)
                    total = 0
                    counter = 0 
            s = res
        return s 



        