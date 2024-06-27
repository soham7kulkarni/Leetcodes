class Solution:
    def isPalindrome(self, s: str) -> bool:

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2 :
            while p1 < p2 and not self.isalnum(s[p1]):
                p1 += 1
            while p2 > p1 and not self.isalnum(s[p2]):
                p2 -= 1 
            if s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                p2 -= 1
        return True 

    def isalnum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')) 


        