# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
       # n1 -> n2 -> n3 -> null
       # null <- n1 <- n2 <-n3
       # we just want to make the previous element in the original LL get pointed at by its original next element. 

        prev = None
        curr = head 
        while curr:
            tmp = curr.next 
            curr.next = prev
            prev = curr
            curr = tmp 
        return prev 