class Solution:
    def trap(self, height: list[int]) -> int:
       # Keep track of the max on the left and right side, we then for each index if the leftMax is less than l, we want to do res += leftMax - left, because given 2 pointers l, r we know that min(heights[l],heights[r]) * (l - r) this is between two points. 

        l = 0 
        r = len(height)-1
        leftMax = height[l]  
        rightMax = height[r]

        res = 0 
        while l <= r:
            if leftMax < rightMax:
                val = height[l]
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                l+=1 
            else:
                val = height[r]
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r-=1
        return res 
