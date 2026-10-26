class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # trivial solution: square elements in array and sort
        # return sorted([x**2 for x in nums])
        
        # two pointer solution 
        res = [0] * len(nums)
        l, r, pos= 0, len(nums)-1, len(nums)-1

        while l <= r: 
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l]**2
                l+=1 
            else:
                res[pos] = nums[r]**2
                r-=1
            pos-=1 
        return res 

