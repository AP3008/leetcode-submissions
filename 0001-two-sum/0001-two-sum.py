class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # targ = nums1 + nums2 => targ - nums1 = nums2
        seen = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in seen:
                return [seen[value], i]
            seen[nums[i]] = i  
        