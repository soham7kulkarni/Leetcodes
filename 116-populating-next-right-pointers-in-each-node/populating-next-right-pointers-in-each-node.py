# Approach - DFS. Connecting leaves with each other and if next node is present in same level then connecting sub trees
# Preorder traversal
# TC - O(N)
# SC - O(1)
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
        self.preorder(root)
        return root
    def preorder(self, root):
        if not root.left: return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.preorder(root.left)
        self.preorder(root.right)
        