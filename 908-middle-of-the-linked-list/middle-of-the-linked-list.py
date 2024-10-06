# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        curr = head
        while curr.next:
            curr = curr.next  
            length+=1
        mid = length//2
        while mid > 0:
            mid-=1
            head = head.next  
        return head
        