# Time Complexity : O(N)
# Space Complexity :O(d), where d is the depth of recursion





# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # Initialize the queue to store the flattened integers
        self.queue = deque()
        # Call DFS helper method to flatten the list
        self.dfs(nestedList)

    def next(self) -> int:
        # Return the front element from the queue and remove it
        return self.queue.popleft()

    def hasNext(self) -> bool:
        # Check if there are any remaining elements in the queue
        return len(self.queue) > 0

    def dfs(self, nestedList: [NestedInteger]):
        # Recursively flatten the nested list
        for ni in nestedList:
            if ni.isInteger():
                # If the element is an integer, add it to the queue
                self.queue.append(ni.getInteger())
            else:
                # If it's a nested list, recursively call dfs on it
                self.dfs(ni.getList())
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())