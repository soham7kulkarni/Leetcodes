# TC - O(N)
# SC - O(N)
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
        if not root: return root  #for null case, we will return empty array
        q = deque([root])   #add root to the linked list
        
        while q:    #We will traverse all the nodes from the current level
            size = len(q)  #For level 0 - size:1, level 1 -  size:2, level 2 - size:4
            prev = None  #Cant link root as successor of any node
            for _ in range(size):  #traversing through all nodes
                curr = q.popleft() #Taking 1 at a time
                
                if prev:   #If we have prev then only we will link our current as next pointer of prev
                    prev.next = curr  #Linking 
                
                if curr.left:  #If we have left node then right exist for sure since its perfect binary tree
                    q.append(curr.left)  #Add left child to the queue
                    q.append(curr.right) #Add right child to the queue
                
                prev = curr  #We auto increment and consider next node in queue hence updating prev to root is imp
                
        return root

        