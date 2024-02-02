# Approach 1 (DFS) - When traversing from left to right, 
# we check if element is already present in result. If yes, we override it with incoming right element
# TC - O(N), SC - O(H)

# Approach 2 (DFS) - If traversing right first and then going to left, no need to overwrite
# TC - O(N), SC - O(H)

# Approach 3 (BFS) - Level order traversal. We traverse till the end of deque/LL and we append last element.
# TC - O(N), SC - O(N) 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#         self.dfs(root, 0, result)
#         return result
#     def dfs(self, root, depth, result):
#         # base
#         if not root: return
#         # action
#         if len(result) == depth:
#             result.append(root.val)
#         else:
#             result[depth] = root.val
#         # treverse left first then right
#         self.dfs(root.left, depth+1, result)
#         self.dfs(root.right, depth+1, result)
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root: return result 
        q = deque()    #Initiating deque/Linked List
        q.append(root) #Adding root (depth = 0)
        while q:
            size = len(q)  #With popleft, length of deque decreses by 1 hence storing size before any modification
            for i in range(0, size):
                curr = q.popleft() #Take 1 node from deque
                if i == size - 1: #If node is last then append it to the result since it is the rightmost element
                    result.append(curr.val)
                if curr.left: q.append(curr.left) #As it is not the rightmost go to his left and add left childrens
                if curr.right: q.append(curr.right)  #As we are done with left, go to his right and add right childrens
        return result


        