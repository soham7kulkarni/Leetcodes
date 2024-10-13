# Approach 1 - putting all elements inside array nd sorting it
# TC - O(nklognk) - nk = n*k (n -> ele in list)(k -> number of list)
# SC - O(nk)

# Approach 2 - using priority queue.
# Putting 1 node of each list inside queue
# Comapring them with each other using heapify
# This helps in mainting least element at top.
# Getting this least element and putting it inside resultant
# Traversing to next node of this node and then putting that next node inside queue
# TC - O(nklogk)
# SC - O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        q = PriorityQueue(maxsize = k)
        dummy = ListNode(None)
        curr = dummy
        for list_idx, node in enumerate(lists):
            if node: q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next

        