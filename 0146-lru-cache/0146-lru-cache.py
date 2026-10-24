class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # we can use dictionary for O(1) lookups and O(1) pops
        #self.cache = {}
        #self.capacity = capacity
        #self.age = collections.deque()

        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        #return self.cache.get(key, -1)
        if key not in self.cache:
            return -1
        node = self.cache[key]
        node.prev.next, node.next.prev = node.next, node.prev

        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        return node.val 
        

    def put(self, key: int, value: int) -> None:
        #if len(self.cache) >= self.capacity:
            #if key is greater than capacity we evict and insert new element
            #oldest = self.age.popleft()
            #del self.cache[oldest]
        # if key exists 
        # if key doesn't exist 
        #self.cache[key] = value
        #self.age.append(key)

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.prev.next, node.next.prev = node.next, node.prev 
        else:
            node = Node(key, value)
            self.cache[key] = node
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        if len(self.cache) > self.capacity:
            lru = self.head.next 
            lru.prev.next, lru.next.prev = lru.next, lru.prev 
            self.cache.pop(lru.key)
        
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)