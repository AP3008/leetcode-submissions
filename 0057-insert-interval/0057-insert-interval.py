class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
       # Just need to go through all of the conditions
       # 1. If the interval doesn't have and overlap between the end of 1 or the start of the following one, we can just insert the interval inbetween 
       # 2. If the interval overlaps between the start and end of an interval, we need to increase the end to our new interval. 
            # 2.1 If the end of the new one overlaps with the start of the following one, we must join the maximum end and this continue as far down as there are collisions on the interval 
        # 3. If the end of our interval overlaps with the start of the following one but the start doesn't overlap with the previous one, meaning our insertion replaces the our new intervals start and the following end. 

        # O(nlogn)
        #intervals.append(newInterval)
        #intervals.sort()
        #res = [intervals[0]]

        #for i in range(1,len(intervals)):
        #    if res[-1][1] >= intervals[i][0]:
        #        res[-1][1] = max(res[-1][1], intervals[i][1])
        #    else:
        #        res.append(intervals[i])
        #return res 

        # O(n)
        # we take the legnth of the array 
        n = len(intervals)
        # This is our output 
        res = []

        # This is the index which tracks where we are in the array, we only do one pass 
        i = 0 
        # While i is within the array and the current intervals end is less than the new intervals start we want to add the interval to our result and increment our pointer because we know that newInterval will be passed these intervals no matter what, so we skip them. 
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1 
        
        # Now we are at the point where we need to either merge the current interval or insert it. So what we can do is create one massive interval and insert it no matter what because we know that it will never intersect with the previous intervals. 

        # If the current interval is within the array and the start of this interval is less than the end of our newInterval we can merge it and take the greater minimum of the two starts, and the greater of the two ends. We do this until it stops being the case at which point this is 100% our new interval we can append. 
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1 
        
        # We add this new interval to our result
        res.append(newInterval)
        # We then add the remaining values from the subararry starting at index i (inclusive) in intervals. I i is the end of the list this extends an empty array doing nothing.
        res.extend(intervals[i:])
        # We return the end of the list. 
        return res 


                