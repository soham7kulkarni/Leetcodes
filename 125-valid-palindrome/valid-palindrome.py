class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            while i < j and not self.isalnum(s[i]):
                i+=1
            while i < j and not self.isalnum(s[j]):
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            else :
                i += 1
                j -= 1
        return True
    
    def isalnum(self, i) -> bool:
        return ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z') or ord('0') <= ord(i) <= ord('9')
        