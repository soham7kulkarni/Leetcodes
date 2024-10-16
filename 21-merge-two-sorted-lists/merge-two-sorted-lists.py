# TC - O(N+M)
# SC - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point of the merged list
        dummy = ListNode()
        # Tail will be used to build the new list
        tail = dummy

        # Traverse both lists and append the smaller value to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Point to the smaller node
                list1 = list1.next  # Move to the next node in list1
            else:
                tail.next = list2  # Point to the smaller node
                list2 = list2.next  # Move to the next node in list2
            tail = tail.next  # Move the tail pointer to the end of the merged list

        # If there are remaining nodes in either list, append them
        if list1:
            tail.next = list1  # Attach the rest of list1 if there are nodes left
        elif list2:
            tail.next = list2  # Attach the rest of list2 if there are nodes left

        # Return the next node of the dummy, which is the head of the merged list
        return dummy.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next



        