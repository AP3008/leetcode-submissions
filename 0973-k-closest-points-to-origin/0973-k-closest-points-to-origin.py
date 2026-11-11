class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # We create a list of elements with tuples as the value we are storing, in the tuple we store the original points at index 1 and the distance away from the origin. Then we put the tuples in a min heap, sorted via the first index of the tuple. Then we pop k elements off the min heap 

        minHeap = [] 
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append((dist, [x,y]))
        
        heapq.heapify(minHeap)
        res = []
        while k:
            res.append(heapq.heappop(minHeap)[1])
            k-=1 
        return res
