class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        bucket = [[] for i in range(len(nums)+1)]
        tracker = {}
        for x in nums:
            tracker[x] = tracker.get(x, 0) + 1
        
        for v, i in tracker.items():
            bucket[i].append(v)
        
        res = []

        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        
        