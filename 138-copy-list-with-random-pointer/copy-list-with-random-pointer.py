"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# TC - O(N)
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
        
        # Preparing copyCurr for traversal thru deep copies
        copyCurr = deepCopyHead
        while curr:

            # 1. Checking if curr has next
            # Then checking if it is in dict
            # If no, creating it in dict
            # Linking the deep copies of curr and curr.next
            if curr.next:
                if curr.next not in node_map:
                    newNode = Node(curr.next.val)
                    node_map[curr.next] = newNode
            # creating deep copy of curr to put in dictionary
            # then linking it as a next node of copyCurr
                copyCurr.next = node_map[curr.next]

            # Same logic, in same pass, checking for random
            if curr.random:
                if curr.random not in node_map:
                    newNode = Node(curr.random.val)
                    node_map[curr.random] = newNode
                copyCurr.random = node_map[curr.random]
            # Trabersing to next nodes
            curr = curr.next
            copyCurr = copyCurr.next

        return deepCopyHead
