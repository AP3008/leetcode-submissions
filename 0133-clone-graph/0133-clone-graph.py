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
        # Iterative loop solution
        if not node:
            return None  
        explore = deque() 
        copies = {}
        explore.append(node)
        while explore:
            nodeToCopy = explore.popleft()
            if nodeToCopy not in copies:
                copies[nodeToCopy] = Node(nodeToCopy.val, [])
            copy = copies[nodeToCopy]
            for n in nodeToCopy.neighbors:
                if n not in copies:
                    copies[n] = Node(n.val, [])
                    explore.append(n)
                copy.neighbors.append(copies[n])
        return copies[node]
                


            
