class MinStack:

    def __init__(self):
       self.minStack = [] 

    def push(self, value: int) -> None:
        minVal = self.getMin()
        if minVal == None or minVal > value:
            minVal = value
        self.minStack.append([value, minVal])

    def pop(self) -> None:
        self.minStack.pop() 

    def top(self) -> int:
        return self.minStack[-1][0] if self.minStack else None 

    def getMin(self) -> int:
        return self.minStack[-1][1] if self.minStack else None 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()