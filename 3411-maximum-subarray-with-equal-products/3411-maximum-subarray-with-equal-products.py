class Solution:
    def maxLength(self, nums: List[int]) -> int:
        # we can use math.gcd() and math.lcm() to get the answer. 
        # We can use a sliding window, whenever we are at a value, we take the window find the lcm, gcd and then the product of the array and see if they match 
        # the length of the array will always be 2. 
        # To keep track of values we can have a current prod. which tracks the product as we shrink the window we divide the left element off, and we multiply the right index on. 
        l = 0
        r = 1 
        curr = nums[0]
        res = 0 
        while r < len(nums):
            curr *= nums[r]
            gcd = math.gcd(*nums[l:r+1])
            lcm = math.lcm(*nums[l:r+1])
            length = r-l+1
            while curr != (gcd*lcm) and l < r:
                curr /= nums[l]
                l+=1 
                length-=1
                gcd = math.gcd(*nums[l:r+1])
                lcm = math.lcm(*nums[l:r+1])
            r+=1 
            res = max(res, length)
        return res 


