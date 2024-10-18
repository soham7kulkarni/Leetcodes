class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Set of vowels for quick lookup
        s_list = list(s)  # Convert the string to a list for mutability
        left, right = 0, len(s) - 1  # Initialize two pointers
        
        while left < right:
            # Move the left pointer to the next vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # Move the right pointer to the previous vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return ''.join(s_list)  # Join the list back into a string