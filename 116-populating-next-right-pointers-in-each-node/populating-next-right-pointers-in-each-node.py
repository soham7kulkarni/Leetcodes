"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            prev = None
            for _ in range(size):
                curr = q.popleft()

                if prev:
                    prev.next = curr

                if curr.left:
                    q.append(curr.left)
                    q.append(curr.right)

                prev = curr

        return root



        