# TC - O(N)
# SC - O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        for j in range(len(t)):
            t_dict[t[j]] = 1 + t_dict.get(t[j], 0)
        
        return s_dict == t_dict
        