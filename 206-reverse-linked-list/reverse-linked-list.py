# Approach - three pointers
# TC - O(N)
# SC - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize three pointers
        prev = None  # This will become the new head of the reversed list
        curr = head  # Start with the head of the original list
        
        # Iterate through the list
        while curr is not None:
            # Save the next node
            next_node = curr.next
            
            # Reverse the current node's pointer
            curr.next = prev
            
            # Move the pointers one step forward
            prev = curr
            curr = next_node
        
        # prev will be the new head of the reversed list
        return prev
        