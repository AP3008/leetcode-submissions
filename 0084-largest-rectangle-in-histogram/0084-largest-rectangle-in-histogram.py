class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # We want to keep track of the maximum area seen. At each index we can take the height of the bar as one area, and compare. We keep a stack storing the heights and starting indexes (we need to find on smaller values), until a height smaller than the value at the top of the stack has been seen. At that point we need to pop all the elements off the stack that are greater than this value, and mutliply it by the starting index and * min(stack.pop(), height[i]) which we know is height[i] otherwise we don't pop. Then whatever the start is of the last value we popped off was that is the start of the index we just put on. We can grab the width by getting Current Index - StackStartValue. At the end of this iteration if the stack has values we can assume that the width will be from the start index to the end of the array and we multiply it by the height to get the area. 

        stack = []
        maxArea = 0 
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i])
            start = i 
            while stack and stack[-1][0] > heights[i]:
                oldHeight, oldStart = stack.pop()
                area = (i-oldStart)*oldHeight
                maxArea = max(maxArea, area)
                start = oldStart 
            stack.append([heights[i], start])
        
        while stack:
            oldHeight, oldStart = stack.pop()
            area = (len(heights)-oldStart)*oldHeight
            maxArea = max(maxArea, area)
        return maxArea 