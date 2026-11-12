class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Brute force intuition: We put each number in a set and check if that set contains n+1 or n-1, but this doesn't really make sense

        # Alt: Since the num.length is 50 we can assume the solution doesn't have great time complexity. We can try and use a sliding window technique, just needs to take into account if we are going down the decreasing subarray path or increasing. 

        if len(nums) <= 1: return 1 
        res = 1 
        for i in range(len(nums)-1):
            length = 1 
            # increasing path 
            while (i+1) < len(nums) and nums[i]+1 <= nums[i+1]:
                length+=1 
                i+=1
            res = max(res, length)
            length = 1  

            # decreasing path
            while (i+1) < len(nums) and nums[i]-1 >= nums[i+1]:
                length+=1 
                i+=1
            res = max(res,length)
        return res 
             
        