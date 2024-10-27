#Linear chaining - array of nodes, inside nodes we have chain of linkedList
#Time Complxity - O(1)
#Worst case we take time to go through all nodes of linked list which here is 100 hence O(1)
#Since we return prev in find for first node we have dummy node (-1,-1) Key is -1 
# since data is positive 
# Put - check the presence of the linked list if not put dummy node. 
# You either hit the end of LL and add fresh node at the end 
# or find exisiting node with same key and updates value
# Get - Check presence of LL. Then check if you are at end or else return node
# Remove - Check presence of LL. Then check if you are at end or else link previous with next one


class MyHashMap:
    # Inner class to define a node for the linked list
    class Node:
        def __init__(self, key, val):
            self.key = key     # Key for the hash map entry
            self.val = val     # Value associated with the key
            self.next = None   # Pointer to the next node in the linked list

    def __init__(self):
        # Initialize the hash map with a fixed number of buckets
        self.buckets = 10000
        # Storage array where each element represents a bucket
        self.storage = [None] * self.buckets

    # Hash function to compute the index for a given key
    def hash1(self, key):
        return key % self.buckets

    # Helper function to find a node with the given key in the linked list
    # Returns the previous node to facilitate operations like add, update, and remove
    def find(self, head, key):
        curr = head           # Start at the head of the linked list
        prev = None           # Initialize previous node to None

        # Traverse until we find the key or reach the end of the list
        while curr and curr.key != key:
            prev = curr       # Move prev to current node
            curr = curr.next  # Move current to next node

        return prev           # Return the previous node, or None if key isn't found

    # Adds a key-value pair to the hash map
    def put(self, key: int, value: int) -> None:
        # Calculate the index for the key using hash function
        bucket = self.hash1(key)
        
        # If no linked list exists at the bucket, initialize it with a dummy node
        if self.storage[bucket] is None:
            self.storage[bucket] = self.Node(-1, -1)  # Dummy node with key -1

        # Find the previous node in the list (or the last node if key doesn't exist)
        prev = self.find(self.storage[bucket], key)

        # If we reached the end and key was not found, create a new node at the end
        if prev.next is None:
            prev.next = self.Node(key, value)
        else:
            # If key exists, update the value
            prev.next.val = value

    # Retrieves the value for a given key; returns -1 if key doesn't exist
    def get(self, key: int) -> int:
        # Calculate the index for the key
        bucket = self.hash1(key)
        
        # If no linked list exists at the bucket, key doesn't exist
        if self.storage[bucket] is None:
            return -1

        # Use find function to locate the previous node
        prev = self.find(self.storage[bucket], key)

        # If key is not in the list, return -1
        if prev.next is None:
            return -1
        else:
            # Return the value of the node with the given key
            return prev.next.val

    # Removes a key-value pair from the hash map
    def remove(self, key: int) -> None:
        # Calculate the index for the key
        bucket = self.hash1(key)
        
        # If no linked list exists at the bucket, there's nothing to remove
        if self.storage[bucket] is None:
            return 
        
        # Use find function to locate the previous node
        prev = self.find(self.storage[bucket], key)

        # If key is not in the list, nothing to remove
        if prev.next is None:
            return
        else:
            # Remove the node by bypassing it in the linked list
            prev.next = prev.next.next
