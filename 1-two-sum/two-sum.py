# Approach 1 - iterating through all numbers for a specific number - O(n^2), O(1)
# Approach 2 - to find pair, we have to find target - num1. Finding in hashmap means finding through keys. Store values in keys and their indexes as values of hashmap. Check if you have difference in hashmap. If yes, return pair or put the number value in key and index in value of hashmap. HASHMAP IS DICTIONARY IN PYTHON - O(N), O(N) 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i
        return
        