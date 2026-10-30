"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # keep track of nodes that have been created with a hashmap, the old node is the key and the new node reference is the value 

        if not node:
            return None

        hashMap = {}
        q = deque() 
        q.append(node)

        while q:
            nodeToCopy = q.popleft()
            if nodeToCopy not in hashMap:
                hashMap[nodeToCopy] = Node(nodeToCopy.val, [])
            n = hashMap[nodeToCopy]
            for nei in nodeToCopy.neighbors:
                if nei not in hashMap:
                    hashMap[nei] = Node(nei.val,[])
                    q.append(nei)
                n.neighbors.append(hashMap[nei])
             
        return hashMap[node]

            
