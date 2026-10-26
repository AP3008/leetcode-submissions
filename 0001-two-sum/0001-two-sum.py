class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = defaultdict() 
        for i in range(len(nums)):
            v = target - nums[i]
            if v in seen:
                return [seen[v], i]
            seen[nums[i]] = i 
        