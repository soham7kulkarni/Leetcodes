# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = prev.next
            if prev == fast:
                return True
        return False
        