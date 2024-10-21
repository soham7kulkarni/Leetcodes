# Approach 1 - 
# Traverse the linked list once to gather all the node values into an array.
# Loop over the first half of the array and calculate the twin sums.
# Return the maximum twin sum.

# TC - O(N)
# SC - O(N)

# Approach 2 - 
# Find the middle of the list using the fast and slow pointer technique.
# Reverse the second half of the linked list.
# Compare nodes from the first and reversed second half to calculate twin sums 
# and keep track of the maximum sum.

# TC - O(N)
# SC - O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        # Step 1: Use two pointers to find the middle of the list (slow and fast pointer)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # slow moves one step
            fast = fast.next.next  # fast moves two steps
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev  # reverse the link
            prev = slow
            slow = temp
        
        # Step 3: Traverse the first and second halves to find the maximum twin sum
        max_twin_sum = 0
        first_half, second_half = head, prev
        while second_half:  # iterate until second_half is not None
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half = first_half.next  # move to the next node in the first half
            second_half = second_half.next  # move to the next node in the reversed second half
        
        return max_twin_sum
        