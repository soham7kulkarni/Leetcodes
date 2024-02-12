# Approach: BFS
# We have to add null(#) in serialization. It helps in keeping track of null
# We can not just go deserialize the string with level 0 = 1 node ,level 1 = 2 node, level 3 = 8 node.
# Its because the tree is not necessarily perfect binary tree.
# Also iterator i is used to assign empty nodes to respective parents. We just don't create empty node. We skip them by incrementing i by 1.
# TC: O(N), SC:O(N)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # If we don't have tree to serialize then return empty string
        if not root: return ""
        # For BFS level order tarversal
        q = deque()
        # Serializing the tree and using # in place of empty nodes
        sb = ""
        q.append(root)
        while q:
            curr = q.popleft()
            if not curr:
                sb+= "#"
            else:
                sb += str(curr.val)
                # Adding children of the node to the queue
                q.append(curr.left)
                q.append(curr.right)
        # For debugging: adding , and printing the result
            sb+= ","
        print(str(sb))
        return sb
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        # Splitting the data on commas
        strArr = data.split(",")
        # Creating Treenode out of string. First converting string node to int node
        root = TreeNode(int(strArr[0]))
        q = deque()
        q.append(root) # root for parents
        # Using i iterator for adding children to root
        i = 1
        while q and i < len(strArr):
            curr = q.popleft()
            # If we hit # just skip by incrementing i by 1

            # left
            if strArr[i] != "#":
                curr.left = TreeNode(int(strArr[i]))
                q.append(curr.left)
            i+=1
            # right
            if strArr[i] != "#":
                curr.right = TreeNode(int(strArr[i]))
                q.append(curr.right)
            i+=1
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))