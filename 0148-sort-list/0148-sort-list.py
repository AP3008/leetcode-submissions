# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head 
        
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next 
            fast = fast.next.next 
        
        prev.next = None
        left = self.sortList(head)
        right =  self.sortList(slow)
        return self.merge(left, right)

    
    def merge(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next 
            else:
                curr.next = l2
                l2 = l2.next 
            curr = curr.next 

        if l1: curr.next = l1
        if l2: curr.next = l2
        return dummy.next 