# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # IDEA: We want to create a hashmap that maps the values of the nodes to the node itself. Then we get a sorted list of the keys (which is the nodes values inorder) and then re-link all of the nodes from the beginning. We use a list[ListNode] as the values of the hashmap because there can be duplicate values, and they need to also join the list, so we need to store both nodes, and loop through the list adding them. 

        # Mapping node value as keys to the node reference in a list 
        nodeMap = defaultdict(list)

        for head in lists:
            curr = head
            while curr:
                nodeMap[curr.val].append(curr)
                curr = curr.next 
        
        # Creating a dummy node as the start of the next list 
        dummy = ListNode()
        curr = dummy 
        # Linking the nodes based of the sorted values 
        for val in sorted(nodeMap.keys()):
            # Each key will have a list, since we don't know how many nodes there are we use a loop
            for node in nodeMap[val]:
                # we set the next node of curr to the node we have taken from the sorted list, and make curr that node, so we can link the remaining nodes
                curr.next = node
                curr = curr.next 
        
        # remove dangling reference 
        curr.next = None

        # Return the list 
        return dummy.next 


