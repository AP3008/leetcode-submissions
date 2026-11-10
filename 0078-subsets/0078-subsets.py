class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # backtracking problem: 
        # build up decision tree from the base empty set
        # Since the length of nums will be less than or equal to 10, we know brute force is the only way.
        res = []
        curr = []

        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            # keeping nums[i]
            dfs(i+1)
            # decision without nums[i]
            curr.pop()
            dfs(i+1)
            return 
        dfs(0)
        return res 

