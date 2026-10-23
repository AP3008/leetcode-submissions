# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # put in a list and remove the nth node from the end 
        curr = head 
        ll = [] 
        while curr:
            ll.append(curr)
            curr = curr.next 
        
        nh = ListNode()
        curr = nh 
        length = len(ll)
        for i in range(len(ll)):
            if i == (length-n):
                continue 
            curr.next = ll[i]
            curr = curr.next 
            curr.next = None
        return nh.next 
