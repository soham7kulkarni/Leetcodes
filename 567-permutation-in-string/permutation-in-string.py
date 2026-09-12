class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) :
             return False
        
        counts1 = [0]*26
        counts2 = [0]*26

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s1), len(s2)):
            if counts1 == counts2:
                return True
            counts2[ord(s2[i]) - ord('a')] += 1
            counts2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        if counts1 == counts2:
            return True
        return False
        