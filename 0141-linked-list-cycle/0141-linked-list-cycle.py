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

       # seen = defaultdict() 
       # while head:
       #     if head in seen:
       #         return True 
       #     seen[head] = 0
       #     head = head.next 

       # return False 

        # better solution uses flynn's cycle detection
        # we have a slow and fast head and wait to see if they intersect. 
        # If they do we return True, otherwise we return Flase 

        if not head:
            return False 
        slow = head 
        fast = head.next 

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next 
            fast = fast.next.next 