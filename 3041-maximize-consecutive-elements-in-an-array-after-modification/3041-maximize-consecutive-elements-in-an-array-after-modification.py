class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # We want to sort the input list so we can iterate from least to greatest 
        nums.sort()
        # Our res at min will always be 1 because we can take one element. 
        res = 1
        # We have a dp hashmap that maps num -> length of largest consecutive sequence
        dp = {}
        # We iterate through the numbers
        for n in nums:
            # We just want to have two variables that store the results of dp n-1 and n. If we do find that either of those values are in dp we want to increase the length of our found sequence by 1. Then we compare to see which of the two is larger a, b, or the current res to see the path that we want to walk down.
            a = b = 1
            if n - 1 in dp:
                a = dp[n-1]+1
            if n in dp:
                b = dp[n]+1
            # We check the max because at this point we don't know if a contains something other than 1. 
            dp[n] = max(dp.get(n,0),a)
            dp[n+1] = max(dp.get(n+1,0),b)
            res = max(res, max(dp[n], dp[n+1]))
        return res 