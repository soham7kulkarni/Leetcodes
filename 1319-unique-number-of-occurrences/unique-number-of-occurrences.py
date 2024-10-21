# TC - O(N)
# SC - O(N)

# Approach - Use counter
# Get all values of counter in dictionary
# Convert the dictionary into set
# If there are duplicate in frequencies then dictionary length will not match with length of set

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Count the frequency of each element in the array
        freq_map = Counter(arr)
        
        # Step 2: Get the frequency values and store them in a set
        frequencies = list(freq_map.values())
        
        # Step 3: Check if all frequencies are unique by comparing the size of the set and the list
        return len(frequencies) == len(set(frequencies))
        