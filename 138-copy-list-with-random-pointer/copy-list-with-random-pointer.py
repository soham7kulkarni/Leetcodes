"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# TC - O(2N)
# SC - O(N)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Base case
        if not head:
            return None
        # Creating deep copy of head
        deepCopyHead = Node(head.val)
        # creating dictionary. It will store original nodes along
        # with deep copies of original nodes
        node_map = {}
        # Using curr to traverse thru original LL
        curr = head
        # Putting first node i.e head inside map
        node_map[curr] = deepCopyHead
        # Going to next 
        curr = curr.next
        # Preparing copyCurr for traversal thru deep copies
        copyCurr = deepCopyHead
        while curr:
            # creating deep copy of curr to put in dictionary
            # then linking it as a next node of copyCurr
            newNode = Node(curr.val)
            node_map[curr] = newNode
            copyCurr.next = newNode
            # Traversing to next node
            curr = curr.next
            copyCurr = copyCurr.next
        # We need to link all random pointers of all deep copies
        curr = head
        copyCurr = deepCopyHead
        while curr:
            # if curr has random
            if curr.random:
                # linking random of copyCurr 
                # with deep copy of node pointed by random of curr
                copyCurr.random = node_map[curr.random]
            curr = curr.next
            copyCurr = copyCurr.next
        return deepCopyHead
