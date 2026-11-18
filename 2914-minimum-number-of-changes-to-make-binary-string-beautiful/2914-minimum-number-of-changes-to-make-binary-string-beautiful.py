class Solution:
    def minChanges(self, s: str) -> int:
        # We can check if a string is beautiful if the len(partition) is 1, if partition is the set of chars in the partition of s. 
        # There are a couple of conditions that we can have an automatic response.
            # 1. If s is odd length we can't partition it evenly. In the conditions is always even so we ignore this
            # 2. If the length  of the set of chars in each partition is 1, it is already beutiful.
        # We can take a greedy approach and just check the current value and the value infornt of it. If it doens't match we need to change it so we increment the counter. Otherwise we can continue because the string is beautiful.  
        counter = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]: counter+=1 
        return counter 