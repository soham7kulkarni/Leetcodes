# TC - O(N)
# SC - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # If the list is empty or has only one node, return None
        if not head or not head.next:
            return None
        
        # Initialize pointers for counting nodes
        slow = head
        fast = head
        prev = None
        count = 0
        
        # Count nodes and find the middle node
        while fast and fast.next:
            fast = fast.next.next  # Move fast pointer two steps
            prev = slow            # Keep track of the previous node
            slow = slow.next       # Move slow pointer one step
            count += 1            # Count the nodes
        
        # Now, slow points to the middle node
        # Adjust the previous node's next pointer to skip the middle node
        if prev:
            prev.next = slow.next
        
        # Return the modified head of the list
        return head
        