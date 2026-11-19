class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Kadane's algo
        globMax = nums[0]
        total = 0
        for n in nums:
            total = max(total + n, n)
            globMax = max(total, globMax)
        return globMax
