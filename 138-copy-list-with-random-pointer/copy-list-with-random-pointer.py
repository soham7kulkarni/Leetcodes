"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_map = {}
        deepCopyHead = Node(head.val)
        node_map[head] = deepCopyHead
        curr = head.next
        copyCurr = deepCopyHead
        while curr:
            newNode = Node(curr.val)
            node_map[curr] = newNode
            curr = curr.next
            copyCurr.next = newNode
            copyCurr = copyCurr.next
        curr = head
        copyCurr = deepCopyHead
        while curr:
            if curr.random:
                copyCurr.random = node_map[curr.random]
            curr = curr.next
            copyCurr = copyCurr.next
        return deepCopyHead
        
        