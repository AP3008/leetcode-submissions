class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap: return ""
        res = ""
        l, r = 0, len(self.timeMap[key])-1
        while l <= r:
            m = (l+r)//2 
            if self.timeMap[key][m][1] <= timestamp:
                res = self.timeMap[key][m][0]
                l = m+1 
            else: r = m-1
        return res 


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)