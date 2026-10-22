class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # hash map sol. 
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen[nums[i]] = i 
            