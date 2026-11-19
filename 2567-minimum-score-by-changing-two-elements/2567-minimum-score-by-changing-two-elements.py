class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # The idea is to sort the list so we can easily find the smallest and largest values. 
        # Since we can change any two elements, we need to find the smallest range among the remaining n-2 elements.
        # There are only 3 remaining test cases
            # Remove the two smallest elements nums[len(nums)-1]-nums[2]
            # Remove the two largest elements: nums[len(nums)-3] - nums[0]
            # Remove the smallest and largest elements: nums[len(nums)-2]-nums[1]
        nums.sort()
        n = len(nums)
        return min(nums[n-1]-nums[2], nums[n-3]-nums[0], nums[n-2]-nums[1])
