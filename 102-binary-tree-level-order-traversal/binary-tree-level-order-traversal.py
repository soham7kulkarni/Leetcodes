# Approach - BFS
# TC - O(N)
# SC - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        result = []
        if not root: return result
        q.put(root)
        while not q.empty():
            li = []
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                li.append(curr.val)
                if curr.left: q.put(curr.left)
                if curr.right: q.put(curr.right)
            result.append(li)
        return result
        