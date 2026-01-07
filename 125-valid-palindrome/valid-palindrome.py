class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        low = 0
        high = n - 1
        while low < high:
            while low < high and not self.isalnum(s[low]):
                low += 1
            while high > low and not self.isalnum(s[high]):
                high -= 1
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True
    def isalnum(self, i) -> bool:
        return ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z') or ord('0') <= ord(i) <= ord('9')
