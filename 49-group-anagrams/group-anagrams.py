# Approach 1 - Take string, sort it, check if the sorted is present in hashmap. 
# If not, create the key and then append a word to that list.
# Next time, dont go back. Just check if sorted word is present in map. 
# If yes, append the word with previously collected words(anagrams). 
# If no, create one. 
# TC - O(n*klogk) - n for traversal, klogk for sorting word
# SC - O(n.k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sort_string = tuple(sorted(s))
            if sort_string in hashmap:
                hashmap[sort_string].append(s)
            else:
                hashmap[sort_string] = [s]
        return list(hashmap.values())
        