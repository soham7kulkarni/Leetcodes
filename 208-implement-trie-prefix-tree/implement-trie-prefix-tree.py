# insert - O(N)
# search - O(N)
# startsWith - O(N)
# SC - O(N)


class TrieNode:
    def __init__(self):
        # Initialize the node with a flag for the end of a word and an array for children
        self.is_end = False
        self.children = [None] * 26  # For each letter a-z

class Trie:
    def __init__(self):
        # Initialize the root of the Trie
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        # Insert a word into the Trie
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')  # Get the index for the character
            if curr.children[index] is None:
                curr.children[index] = TrieNode()  # Create a new node if it doesn't exist
            curr = curr.children[index]  # Move to the child node
        curr.is_end = True  # Mark the end of the word
    
    def search(self, word: str) -> bool:
        # Search for a word in the Trie
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')  # Get the index for the character
            if curr.children[index] is None:
                return False  # Character not found
            curr = curr.children[index]  # Move to the child node
        return curr.is_end  # Return True if it's the end of a word
    
    def startsWith(self, prefix: str) -> bool:
        # Check if there is any word in the Trie that starts with the given prefix
        curr = self.root
        for char in prefix:
            index = ord(char) - ord('a')  # Get the index for the character
            if curr.children[index] is None:
                return False  # Character not found
            curr = curr.children[index]  # Move to the child node
        return True  # Prefix found

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)