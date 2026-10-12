# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        stack = list()
        while curr:
            if curr in stack:
                return curr 
            stack.append(curr)
            curr = curr.next 
        return None 

        