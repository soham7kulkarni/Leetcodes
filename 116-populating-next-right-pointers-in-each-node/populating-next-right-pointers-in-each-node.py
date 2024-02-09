# TC - O(N)
# SC - O(1)
# Approach - Two pointers. Level pointer for level traversal and curr pointer. 
# Utilizing next pointer of the nodes
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
        level = root #Assigning root to level pointer
        while level.left: #We dont want to traverse leaf node only parent nodes
            curr = level #Assigning start of every level to curr pointer
            while curr:
                curr.left.next = curr.right #if curr exist, both leaves exist, linking them
                if curr.next: #if 2 and 3 both exist, then linking between two subtrees
                    curr.right.next = curr.next.left
                curr = curr.next #traversing to next curr from 2 to 3
            level = level.left #After 3, level completed hence moving to next level i.e left of level
        return root
            
                

        