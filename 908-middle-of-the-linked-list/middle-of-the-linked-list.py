# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        temp = head
        while temp.next is not None:
            length+=1
            temp = temp.next
        mid = length // 2
        # print(mid)
        # print(head)
        while mid > 0 :
            head = head.next
            mid-=1
        return head


        

        