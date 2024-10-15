class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = x
        result = 0
        while x > 0:
            temp = x%10
            result = result*10 + temp
            x = x//10
        return rev == result
    

        