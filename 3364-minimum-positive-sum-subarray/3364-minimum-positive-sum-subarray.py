class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # We can have negatives, the size of the array is at min l and at max r and the sum has to be greater than 0 or we return -1 
        # IDEA: We scan through the array until we get a height of l, by incrementing the right pointer, once we find a subarray of length l, then we can see if it is a valid value, we increase until we get a subarray of length r, there is a case when r is at the end of the array but we haven't checked the subarray of size l at the end which could be greater.

        # TRY A PREFIX SUM IDEA, WE COLLECT AND SUBTRACT AS WE SEE ELEMENTS, THAT ARE WITHIN THE WINDOW.  
        
        # If we have this impossible case we can return -1 
        if len(nums) < l: return -1 

        # We build the prefix list that is one element longer than nums. Each entry represents the sum of all elements that appear before that position 
        prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        #We create our minimum as infinity, so we can use the min function properly. 
        minSum = float('inf')
        
        # We want to iterate over all possible right end points, which will start at l and end at the end of the array. We start at l because we can't use a subarray that hasn't taken at least l elements
        for right in range(l, len(nums)+1):
            # Now we iterate through every valid length which is between l and r. We use min(r,right) because a subarray ending at exclusive index right cannot have more than right elements
            for length in range(l, min(r, right)+1):
                # We need to find the left endpoint since we already know the right endpoint and the length of the current string we can just take the length away from the right endpoint to know where the left end point needs to be. 
                left = right - length 
                # The current sum is the sum of all elements before the right endpoint - all the elements before the left endpoint. This leaves us with the sum of elements between left and right. 
                currSum = prefix[right]-prefix[left]
                # If the value is greater than 0 we can check if this is our current min 
                if currSum > 0:
                    minSum = min(minSum, currSum)
        # If we got a minSum that was greater than zero we can return it, otherwise we return -1.
        return minSum if minSum != float('inf') else -1 