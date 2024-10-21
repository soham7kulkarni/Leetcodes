# Approach - Traverse through the nodes
# If node index is even, link even.next to this node nd increment even ptr
# If node index is odd, link odd.next to this node nd increment odd ptr

# TC - O(N)
# SC - O(1)




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If the list is empty or has only one node, return the head as is
        if head == None or head.next == None:
            return head 
        
        # Create two dummy nodes for odd and even indexed lists
        odd = ListNode(0)  # Dummy node for odd indexed nodes
        odd_ptr = odd      # Pointer to construct the odd list
        even = ListNode(0) # Dummy node for even indexed nodes
        even_ptr = even    # Pointer to construct the even list
        
        idx = 1  # Initialize the index to track whether the node is odd or even
        
        # Traverse the original linked list
        while head != None:
            if idx % 2 == 0:  # If the index is even
                even_ptr.next = head  # Link the even pointer to the current node
                even_ptr = even_ptr.next  # Move the even pointer to the next node
            else:  # If the index is odd
                odd_ptr.next = head  # Link the odd pointer to the current node
                odd_ptr = odd_ptr.next  # Move the odd pointer to the next node
            
            head = head.next  # Move to the next node in the original list
            idx += 1  # Increment the index
        
        # Terminate the even list
        even_ptr.next = None
        
        # Link the odd list with the even list
        odd_ptr.next = even.next  # Connect the end of odd list to the head of even list
        
        # Return the head of the odd indexed list, which is the next of the dummy node
        return odd.next
