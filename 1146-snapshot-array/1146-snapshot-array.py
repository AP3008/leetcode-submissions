class SnapshotArray:
    # THIS DOESN'T WORK BECAUSE OF SPACE, BUT ALGO IS CORRECT.

    def __init__(self, length: int):
        #self.snapMap = {}
        #self.arr = [0] * length        
        #self.snapCount = -1

        self.A = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        #if 0 <= index < len(self.arr):
        #    self.arr[index] = val
        self.A[index].append([self.snap_id, val])

    def snap(self) -> int:
        # Need to make a copy and not use reference to same array in memory
        #tmp = self.arr.copy()
        #self.snapCount+=1
        #self.snapMap[self.snapCount] = tmp
        #return self.snapCount

        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        #if 0 <= index < len(self.arr):
        #    return self.snapMap[snap_id][index]

        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)