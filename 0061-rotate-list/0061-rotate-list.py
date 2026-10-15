# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        # Thoughts: if n = len(list) => same rotation, k can be really big so we most likely just want to use mod to try and figure out how many rotations we actually need to do. I am thinking of using a function that rotates once 

        # Go until k - 1 stacking appending elements to a list, then the k-1'th node points to null, and k points to the front of the list. And return the kth node a the head. Just need to go over edge cases

        # Edge cases, if n mod len(list) the list needs to remain the same, which if we apply the k-1th rule would still be valid. 

        if not head:
            return None 

        length = 1
        tmp = head 
        while tmp.next:
            tmp = tmp.next 
            length+=1 
        
        rotation = k % length 
        if rotation == 0:
            return head
        
        curr = head
        for i in range(length-rotation-1):
            curr = curr.next 
        
        newHead = curr.next 
        curr.next = None
        tmp.next = head 

        return newHead 