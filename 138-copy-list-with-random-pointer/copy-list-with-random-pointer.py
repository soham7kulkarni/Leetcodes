"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# TC - O(3N)
# SC - O(1)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Created the deep copy of nodes alongside the og nodes
        curr = head
        while curr:
            copyCurr = Node(curr.val)
            copyCurr.next = curr.next
            curr.next = copyCurr
            curr = curr.next.next
        # Creating random pointers on deep copy nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next #Pointing to deep copy of random
            curr = curr.next.next
        
        # Splitting the two lists
        curr = head
        deepCopyHead = head.next
        copyCurr = deepCopyHead
        while curr:
            curr.next = curr.next.next
            if copyCurr.next:
                copyCurr.next = copyCurr.next.next
            curr = curr.next
            copyCurr = copyCurr.next
        return deepCopyHead

