# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        first = head
        while first:
            nxt = first.next
            first.next = prev
            prev = first
            first = nxt
        return prev
        