class Node:
    def __init__(self, key, value):
        # Initialize a node with a given key and value
        self.key = key
        self.value = value
        self.prev = None  # Pointer to the previous node in the doubly linked list
        self.next = None  # Pointer to the next node in the doubly linked list


class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the LRU Cache with a given capacity
        self.capacity = capacity
        self.cache = {}  # HashMap to store key-node pairs for O(1) access

        # Create dummy head and tail nodes to represent the boundaries of the doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # Link head and tail together initially
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        # Disconnect a node from its current position in the doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        # Add a new node right after the head to mark it as most recently used
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            # Return -1 if the key is not in the cache
            return -1
        # Retrieve the node from the HashMap
        node = self.cache[key]

        # Since node is accessed, move it to the head (most recently used)
        self._remove_node(node)
        self._add_to_head(node)

        # Return the value associated with the node
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key already exists, update the node's value
            node = self.cache[key]
            node.value = value

            # Move the node to the head to mark it as recently used
            self._remove_node(node)
            self._add_to_head(node)
        else:
            # If the key doesn't exist, create a new node
            new_node = Node(key, value)

            # Add the new node to the HashMap and the head of the list
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # Check if the cache has exceeded its capacity
            if len(self.cache) > self.capacity:
                # Remove the least recently used node (node before the tail)
                lru_node = self.tail.prev
                self._remove_node(lru_node)

                # Remove the LRU node from the HashMap
                del self.cache[lru_node.key]
