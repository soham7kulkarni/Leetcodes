# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if i == n-1:
                    result.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
        return result


        