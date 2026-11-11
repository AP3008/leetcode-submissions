class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) <= 1: return 0 if not nums else nums[0]
        total = 0
        res = float('-inf')
        for n in nums:
            total += n
            res = max(res,total)
            if total < 0:
                total = 0
        return res 
