class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # hash map sol. 
        #seen = {}
        #for i in range(len(nums)):
        #    if nums[i] in seen:
        #        return nums[i]
        #    seen[nums[i]] = i 

        # cycle detection because nums[i] is within 1 -> n
        tortise = nums[0]
        hare = nums[nums[0]]

        while tortise != hare:
            tortise = nums[tortise]
            hare = nums[nums[hare]]
        
        tortise = 0
        while tortise != hare:
            tortise = nums[tortise]
            hare = nums[hare]

        return hare 