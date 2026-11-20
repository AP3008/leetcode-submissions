class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # Iterate backwards from last square to see if it is possible to reach the goal. Assume the goal is at the end, if we can move the goal post ahead we are trying to see if it is possible to make the start and goal the same. 
        # We can do this by checking the elements of the array backwards, if it is possible from that square to reach the goal, we can move the goal to that square. We do this until we get to the beginning of the array. 

        goal = len(nums)-1
        for i in range(len(nums)-1, -1,-1):
            if nums[i] + i >= goal:
                goal = i
            if goal == 0: return True 
        return False 