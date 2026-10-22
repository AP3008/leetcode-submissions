# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Splits list in half 
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # reversing second half of linked list from mid + 1 index
        second = slow.next 
        prev = slow.next = None
        
        while second:
            tmp = second.next 
            second.next = prev
            prev = second
            second = tmp
        
        # taking first part of linkedlist and alternating it with the reversed second half, when the second half is done we will be at the half way point of the original linkedlist and the list will look reordered
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next 
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 


            
        