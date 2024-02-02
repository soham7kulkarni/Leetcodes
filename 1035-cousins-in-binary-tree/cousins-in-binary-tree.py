# Approach (BFS) - Two deques. One for nodes. One for parents. 1:1 mapping
# Check if nodes share same parent, or belong to same level or else immediate False
# Both will always belong to same depth. hence when we found both, mark flags as True and their parents.
# If both flags are true, it means both found on same level. Just check the parents.
# If we found just 1 on that level immediate False.
# TC - O(N), SC - O(N)

# Approach 2 - when you don't want to use another deque, everytime we enter the children of the root node,
# If both are x and y, immediate False


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
        q.append(root)
        pq.append(None)
        while q:
            size = len(q)
            x_found = False
            y_found = False
            for i in range(size):
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
            if x_found and y_found: return px != py
            if x_found or y_found: return False
        return False


# class Solution:
#     def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
#         q = deque() 
#         q.append(root)
       
#         while q:
#             size = len(q)
#             x_found = False
#             y_found = False
#             for i in range(size):
#                 curr = q.popleft()
                
#                 if curr.val == x:
#                     x_found = True
                   
#                 if curr.val == y:
#                     y_found = True
                  
#                 if curr.left and curr.right:
#                     if curr.left.val == x and curr.right.val == y: return False
#                 if curr.left: 
#                     q.append(curr.left)
#                 if curr.right: 
#                     q.append(curr.right)
                    
#             if x_found and y_found: return True
#             if x_found or y_found: return False
#         return False



