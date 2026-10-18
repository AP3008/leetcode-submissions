class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return not len(set(nums)) == len(nums)

        seen = {}
        for x in nums:
            if x in seen:
                return True 
            seen[x] = True 
        return False 