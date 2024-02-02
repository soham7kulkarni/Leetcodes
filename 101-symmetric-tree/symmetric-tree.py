# Approach 1 (DFS) - We go to left's left and then right's right. 
# After we go to left's right and right's left.
# When we are at leaf, both are null, just return
# When any one of them is null or they are not same, we return False
# Or else we return True
# TC - O(N), SC - O(H)

# Approach 2 (BFS) - Use stack or queue. Add root. Add left and right child to queue.
# Check if pushed children are equal. If not, immediate False. Or else, check till end.
# TC - O(N), SC - O(N)
# If we check the given level is palindrome or not, place the null spaces carefully.
# Instead checking if 5445 is same as 5445 (Here we don't know if value is left child or right child) 
# Just check 55 then 44.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.flag = True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        self.flag = True
        self.dfs(root.left, root.right)
        return self.flag
    def dfs(self, left, right):
        # base
        if left is None and right is None: return
        # logic
        if left is None or right is None or left.val != right.val:
            self.flag = False
            return
        if self.flag:
            self.dfs(left.left, right.right)
        if self.flag:
            self.dfs(left.right, right.left)
        
        
        