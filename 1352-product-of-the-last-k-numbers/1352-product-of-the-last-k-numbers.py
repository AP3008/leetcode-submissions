class ProductOfNumbers: 
    # O(n) solution first then we push for O(1) - Didn't pass but simple
    # We store a tuple at each element, holding the total product up till that value
    # This Almost works because, it fails at products of zero, then everything following becomes zero. 
    def __init__(self):
        self.stream = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
        else:
            self.stream.append(self.stream[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.stream): return 0
        return self.stream[-1]//self.stream[-k-1]
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)