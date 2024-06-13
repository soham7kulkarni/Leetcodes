class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)
        for i in s:
            a[i]+=1
        for j in t:
            b[j]+=1
        if a == b:
            return True
        else:
            return False

        