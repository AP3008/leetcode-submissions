# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # hash map sol. 
        visited = defaultdict() 
        curr = head 
        position = 0 
        while curr:
            if curr in visited:
                return curr 
            visited[curr] = position 
            curr = curr.next 
            position += 1
        return None

        