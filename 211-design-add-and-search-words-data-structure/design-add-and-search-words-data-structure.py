# The space complexity is O(n), 
# where n is the total number of characters in all words stored in the Trie. 
# Each character requires its own node in the Trie.

# Time complexity is O(n) where n is length of word to be searched


# Define a TrieNode class to represent each node in the Trie.
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children and a flag to indicate if it marks the end of a word
        self.children = {}
        self.is_word = False

# Define the WordDictionary class that uses the TrieNode structure.
class WordDictionary:
    def __init__(self):
        # Initialize the root node of the Trie.
        self.root = TrieNode()

    # Method to add a word to the Trie.
    def addWord(self, word):
        current_node = self.root  # Start from the root node.
        
        # Iterate through each character in the word.
        for character in word:
            # Set default if character doesn't exist in the current node's children, move to the next node.
            current_node = current_node.children.setdefault(character, TrieNode())
        
        # After inserting all characters, mark the last node as a word-ending node.
        current_node.is_word = True

    # Method to search for a word in the Trie, including support for the wildcard character '.'.
    def search(self, word):
        # Define a helper function to perform a depth-first search (DFS) on the Trie.
        def dfs(node, index):
            # If we have checked all characters (i.e., index == length of the word), return if we're at a word-ending node.
            if index == len(word):
                return node.is_word
            
            # If the current character is a '.', it can match any character.
            if word[index] == ".":
                # Try all possible children nodes (since '.' can be any letter).
                for child in node.children.values():
                    # Recursively search for the next character in each child node.
                    if dfs(child, index + 1):
                        return True  # If any path matches, return True.
            else:
                # If the current character is not a '.', check if it's in the current node's children.
                if word[index] in node.children:
                    # Recursively search in the matching child node for the next character.
                    return dfs(node.children[word[index]], index + 1)
            
            # If no match is found, return False.
            return False

        # Start the DFS from the root node and index 0 (first character of the word).
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)