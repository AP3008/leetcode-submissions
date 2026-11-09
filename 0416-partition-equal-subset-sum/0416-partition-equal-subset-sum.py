class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2: return False 
        target = sum(nums)//2
        sett = set()
        sett.add(0)
        for n in nums:
            newSet = set()
            for s in sett:
                newSet.add(n+s)
                newSet.add(s)
            sett = newSet 
        return True if target in sett else False 
