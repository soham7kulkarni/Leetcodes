# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        pq = deque()
        px, py = None, None
        x_found, y_found = False, False
        q.append(root)
        pq.append(None)
        while q:

            n = len(q)
            for i in range(n):
                curr = q.popleft()
                parent = pq.popleft()
                if curr.val == x:
                    x_found = True
                    px = parent
                if curr.val == y:
                    y_found = True
                    py = parent
                if curr.left:
                    q.append(curr.left)
                    pq.append(curr)
                if curr.right:
                    q.append(curr.right)
                    pq.append(curr)

            if x_found and y_found: return px!= py
            if x_found or y_found: return False
            
        return False
                
        