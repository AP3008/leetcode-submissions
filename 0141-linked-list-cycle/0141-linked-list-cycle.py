# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two solutions
        # Simple sol. uses a hash map
        # 1. Track all of the nodes that have been seen, if a node is already in the hashmap, then we return true, because there is a cycle. 

        seen = defaultdict() 
        while head:
            if head in seen:
                return True 
            seen[head] = 0
            head = head.next 

        return False 