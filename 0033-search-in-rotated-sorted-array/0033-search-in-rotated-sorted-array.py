class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # find pivot, binary search 
        l, r = 0, len(nums)-1
        while l <= r:
            # m = 0 
            m = (l+r) //2 # 0, 1, 1, 
            if nums[m] == target: # 3 != 5 
                return m 

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1 # since we know this side is sorted properly, we search here
                else:
                    l = m + 1 # if target is not less than nums[m] or target is smaller than nums[l] we know we aren't searching the correct side, meaning we move the left pointer up. 
            else: # if our mid is not in a sorted half we enter this portion 
                if nums[m] < target <= nums[r]: # If the right side of mid is sorted we can increment the left pointer to mid and we know that target is somehwere inbetween 
                    l = m + 1 
                else: # Otherwise we want to explore the other side. 
                    r = m - 1
        return -1 